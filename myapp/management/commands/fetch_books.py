import os
import tempfile
import urllib.request
from django.core.management.base import BaseCommand
from myapp.models import Book, Person
from bs4 import BeautifulSoup

class Command(BaseCommand):
    help = 'Fetches books from Project Gutenberg and stores them in the database.'

    def handle(self, *args, **options):
        urls = [
            'https://www.gutenberg.org/files/1342/1342-h/1342-h.htm',
            'https://www.gutenberg.org/files/11/11-h/11-h.htm',
            # Add more URLs as needed
        ]

        for url in urls:
            with tempfile.TemporaryDirectory() as temp_dir:
                download_path = os.path.join(temp_dir, 'book.html')

                # Download the HTML file
                urllib.request.urlretrieve(url, download_path)

                try:
                    # Extract information from the HTML file
                    with open(download_path, 'r', encoding='utf-8') as html_file:
                        html_content = html_file.read()
                        soup = BeautifulSoup(html_content, 'html.parser')

                        # Extract title and author if they exist
                        title_element = soup.find('h1')
                        author_element = soup.find('p', class_='author')

                        title = title_element.text.strip() if title_element else None
                        author_name = author_element.text.strip() if author_element else None

                        # Get or create the author object
                        author, _ = Person.objects.get_or_create(name=author_name)

                        # Create or update Book object in the database
                        book, created = Book.objects.update_or_create(
                            title=title,
                            defaults={'authors': [author]} if author else None,
                        )

                        if created:
                            self.stdout.write(self.style.SUCCESS(f'Created book "{book.title}"'))
                        else:
                            self.stdout.write(self.style.SUCCESS(f'Updated book "{book.title}"'))

                except Exception as e:
                    self.stderr.write(self.style.ERROR(f'Error processing URL {url}: {e}'))

                # Clean up downloaded file
                os.remove(download_path)

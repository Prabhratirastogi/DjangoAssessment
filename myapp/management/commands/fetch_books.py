import os
from django.core.management.base import BaseCommand
from myapp.models import Book
import urllib.request
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
        download_path = 'book.html'

        # Download the HTML file
        urllib.request.urlretrieve(url, download_path)

        # Extract information from the HTML file
        with open(download_path, 'r', encoding='utf-8') as html_file:
            html_content = html_file.read()
            # Assuming you use BeautifulSoup for HTML parsing
            soup = BeautifulSoup(html_content, 'html.parser')
            
            # Debugging: Print the soup content to check if the author element is found
            print(soup)

            # Extract title and author if they exist
            title_element = soup.find('h1')
            author_element = soup.find('p', class_='author')

            if title_element:
                title = title_element.text.strip()
            else:
                title = None

            if author_element:
                author = author_element.text.strip()
            else:
                author = None

            # Create or update Book object in the database
            book, created = Book.objects.update_or_create(
                title=title,
                defaults={
                    'author': author,
                    # Add other fields as needed
                }
            )

            if created:
                self.stdout.write(self.style.SUCCESS(f'Created book "{book.title}"'))
            else:
                self.stdout.write(self.style.SUCCESS(f'Updated book "{book.title}"'))

        # Clean up downloaded file
        os.remove(download_path)

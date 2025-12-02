"""
Formatter module
Provides formatting utilities for currency, dates, and more
"""

from datetime import datetime


def format_currency(amount, currency="$"):
    """Format number as currency"""
    return f"{currency}{amount:,.2f}"


def format_date(date_obj=None, format_str="%Y-%m-%d"):
    """Format datetime object as string"""
    if date_obj is None:
        date_obj = datetime.now()
    return date_obj.strftime(format_str)


def format_percentage(value, decimal_places=2):
    """Format number as percentage"""
    return f"{value:.{decimal_places}f}%"


def format_phone(phone_number):
    """Format phone number (US format)"""
    # Remove non-digits
    digits = "".join(filter(str.isdigit, str(phone_number)))
    if len(digits) == 10:
        return f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"
    return phone_number


def format_name(first_name, last_name):
    """Format full name"""
    return f"{first_name.title()} {last_name.title()}"


def format_file_size(size_bytes):
    """Format file size in human-readable format"""
    for unit in ["B", "KB", "MB", "GB", "TB"]:
        if size_bytes < 1024.0:
            return f"{size_bytes:.2f} {unit}"
        size_bytes /= 1024.0
    return f"{size_bytes:.2f} PB"


def truncate_text(text, max_length=50, suffix="..."):
    """Truncate text to max length"""
    if len(text) <= max_length:
        return text
    return text[: max_length - len(suffix)] + suffix


if __name__ == "__main__":
    print("Formatter Module Test")
    print(f"Currency: {format_currency(1234.56)}")
    print(f"Date: {format_date()}")
    print(f"Percentage: {format_percentage(75.5)}")
    print(f"Phone: {format_phone('1234567890')}")
    print(f"Name: {format_name('john', 'doe')}")
    print(f"File Size: {format_file_size(1536000)}")
    print(
        f"Truncate: {truncate_text('This is a very long text that needs truncation', 20)}"
    )

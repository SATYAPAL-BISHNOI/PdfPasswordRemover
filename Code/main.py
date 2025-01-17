


import PyPDF2
import itertools
import string
import time

def try_password(pdf_reader, password):
    try:
        if pdf_reader.decrypt(password) == 1:
            return True
    except:
        return False
    return False

def brute_force_pdf(pdf_path, max_length):
    chars = string.ascii_letters + string.digits + string.punctuation
    pdf_reader = PyPDF2.PdfReader(pdf_path)
    
    if not pdf_reader.is_encrypted:
        print("PDF is not password protected.")
        return None
    
    for length in range(1, max_length + 1):
        for guess in itertools.product(chars, repeat=length):
            password = ''.join(guess)
            if try_password(pdf_reader, password):
                print(f"Password found: {password}")
                return password
            print(f"Tried password: {password} {guess}")

    print("Password not found within the given length constraints.")
    return None

def remove_password(pdf_path, password, output_path):
    pdf_reader = PyPDF2.PdfReader(pdf_path)
    pdf_reader.decrypt(password)
    pdf_writer = PyPDF2.PdfWriter()
    
    for page_num in range(len(pdf_reader.pages)):
        pdf_writer.add_page(pdf_reader.pages[page_num])
    
    with open(output_path, 'wb') as output_pdf:
        pdf_writer.write(output_pdf)
    print(f"Decrypted PDF saved to {output_path}")
name = "main"
if name == "main":
    pdf_path = 'pdf1.pdf'  # Replace with your PDF file path
    output_path = 'decrypted_pdf.pdf'  # Path for the decrypted PDF
    max_length = 30  # Set this to the maximum length of the password you want to try
    start_time = time.time()
    
    password = brute_force_pdf(pdf_path, max_length)
    if password:
        remove_password(pdf_path, password, output_path)
    
    end_time = time.time()
    print(f"Time taken: {end_time - start_time} seconds")





    #this code in havay time complextiy you have this code :-








                # you will use this down code than upper code CommentOut



import PyPDF2
import itertools
import string
import multiprocessing
import time

def try_password(pdf_path, password):
    pdf_reader = PyPDF2.PdfReader(pdf_path)
    try:
        if pdf_reader.decrypt(password) == 1:
            return password
    except:
        return None
    return None

def brute_force_worker(pdf_path, chars, length, queue):
    for guess in itertools.product(chars, repeat=length):
        password = ''.join(guess)
        result = try_password(pdf_path, password)
        if result:
            queue.put(result)
            return
        print(f"Tried password: {password}")

def brute_force_pdf(pdf_path, max_length, charset, timeout):
    pdf_reader = PyPDF2.PdfReader(pdf_path)
    
    if not pdf_reader.is_encrypted:
        print("PDF is not password protected.")
        return None
    
    queue = multiprocessing.Queue()
    processes = []
    start_time = time.time()

    for length in range(1, max_length + 1):
        p = multiprocessing.Process(target=brute_force_worker, args=(pdf_path, charset, length, queue))
        processes.append(p)
        p.start()

    for p in processes:
        p.join(timeout)  # Limit time for each process

    if not queue.empty():
        password = queue.get()
        print(f"Password found: {password}")
        return password

    print("Password not found within the given length constraints.")
    return None

def remove_password(pdf_path, password, output_path):
    pdf_reader = PyPDF2.PdfReader(pdf_path)
    pdf_reader.decrypt(password)
    pdf_writer = PyPDF2.PdfWriter()
    
    for page_num in range(len(pdf_reader.pages)):
        pdf_writer.add_page(pdf_reader.pages[page_num])
    
    with open(output_path, 'wb') as output_pdf:
        pdf_writer.write(output_pdf)
    print(f"Decrypted PDF saved to {output_path}")

if __name__ == "__main__":
    pdf_path = 'pdf1.pdf'  # Replace with your PDF file path
    output_path = 'decrypted_pdf.pdf'  # Path for the decrypted PDF
    max_length = 19  # Limit password length to reduce complexity
    charset = string.ascii_lowercase + string.digits + string.punctuation # Limit character set
    timeout = 3000  # Limit total time to 50 minutes (300 seconds)

    start_time = time.time()
    
    # Run brute force attack with limited charset and length
    password = brute_force_pdf(pdf_path, max_length, charset, timeout)
    
    if password:
        remove_password(pdf_path, password, output_path)
    
    end_time = time.time()
    print(f"Time taken: {end_time - start_time} seconds")































































































# import PyPDF2
# import itertools
# import string

# def brute_force_pdf_password(pdf_path, max_length=10):
#     pdf_reader = PyPDF2.PdfFileReader(pdf_path)

#     # Define the character set (you can customize this)
#     charset = string.ascii_letters + string.digits

#     # Try all combinations of the defined character set up to max_length
#     for length in range(1, max_length + 1):
#         for attempt in itertools.product(charset, repeat=length):
#             password = ''.join(attempt)
#             print(f"Trying password: {password}")
#             if pdf_reader.decrypt(password) == 1:
#                 print(f"Password found: {password}")
#                 return password

#     print("Password not found within the given length.")
#     return None

# brute_force_pdf_password("/pdf1.pdf",max_length=10)
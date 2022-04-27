import io

# Write to a buffer.
output = io.BytesIO()
output.write('This goes into the buffer. '.encode('utf-8'))
output.write('ÁÇÊ'.encode('utf-8'))

# Retrieve the value written.
print(output.getvalue())

output.close()  # Discard buffer memory.

# Initialize a read buffer.
input = io.BytesIO(b'Inital value for read buffer')

# Read from the buffer.
print(input.read())

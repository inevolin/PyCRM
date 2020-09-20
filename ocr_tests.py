import ocr

testfile = './demo_files/doc1.pdf'
print('testing: %s' % testfile)
out = ocr.process(testfile)
assert 'CONTRACT FOR SOFTWARE PROGRAMMING SERVICES' in out
print('OK!')

testfile = './demo_files/doc2.pdf'
print('testing: %s' % testfile)
out = ocr.process(testfile)
assert 'Invoice' in out
print('OK!')

testfile = './demo_files/doc2.pdf'
print('testing: %s' % testfile)
out = ocr.process(testfile, pdf_method=1)
assert 'Invoice' in out
print('OK!')

testfile = './demo_files/doc3.pdf'
print('testing: %s' % testfile)
out = ocr.process(testfile)
assert len(out) == 0
print('OK!')

testfile = './demo_files/doc3.pdf'
print('testing: %s' % testfile)
out = ocr.process(testfile, pdf_method=1)
assert 'invoice' in out and len(out) > 10
print('OK!')

testfile = './demo_files/doc1.docx'
print('testing: %s' % testfile)
out = ocr.process(testfile)
assert 'contract' in out and 'Party A' in out and 'Party B' in out
print('OK!')

testfile = './demo_files/pass1.jpg'
print('testing: %s' % testfile)
out = ocr.process(testfile)
assert 'PASSPORT' in out and 'CANADA' in out
print('OK!')

testfile = './demo_files/pass2.jpg'
print('testing: %s' % testfile)
out = ocr.process(testfile)
assert 'U.S.A' in out
print('OK!')



print('All tests succeeded!')
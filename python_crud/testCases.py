from python_crud import arrayMethods

# If the arguments (i.e. The list of elements) are not passed to arrayMethods() class, It'll be initialized with empty list automatically
testCase1 = arrayMethods()

# Add element
ad1 = testCase1.add_element(2)
ad2 = testCase1.add_element('John Doe',1)
ad3 = testCase1.add_element(567.984,0)

# Update element
# up1 = testCase1.update_element(2)
up2 = testCase1.update_element('John Doe','arnold')
up3 = testCase1.update_element(567.984,0)

# Remove element
rm1 = testCase1.remove_element('arnold',by_index=True)

# Clear array
cl1 = testCase1.clear_array()


testResult = testCase1.read_array()
print(testResult)

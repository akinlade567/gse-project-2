# Sample data file
def creat_test_files():

    # Create numerical data file (CSV format)
    with open('test_scores.CSV', 'w') as f:
        f.write("""85, 92, 78, 88, 95
67, 74, 89, 92, 82
76, 84, 79, 93, 88
55, 68, 72, 90, 87             
94, 81, 77, 85, 96""")
        
    # Create categorical data file
    with open('test_categories.txt', 'w') as f:
            f.write("""Mathematics
Physics
Chemistry
Mathematics
Biology
Physics
Computer Science
Mathematics
Chemistry
Physics
Biology
Arts""")
            
    # Create empty file for testing error handline
    with open('empty_file.text', 'w') as f:
         pass
    
    print("Test files created successfully:")
    print("1. test_scores.csv - Numerical data")
    print("2. test_categories.txt - Categorical data")
    print("3. empty_file.txt - Empty file for testing")

if __name__ == "_main_":
     creat_test_files

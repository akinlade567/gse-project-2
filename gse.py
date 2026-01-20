import csv
import os

# ==================== FUNCTIONS FOR TASK 3 ====================
def calculate_total(data):
    """Calculate the total sum of numerical data"""
    total = 0
    for value in data:
        total += value
    return total

def calculate_average(data):
    """Calculate the average of numerical data"""
    if len(data) == 0:
        return 0
    total = calculate_total(data)
    return total / len(data)

def calculate_minimum(data):
    """Find the minimum value in the data"""
    if len(data) == 0:
        return None
    minimum = data[0]
    for value in data[1:]:
        if value < minimum:
            minimum = value
    return minimum

def calculate_maximum(data):
    """Find the maximum value in the data"""
    if len(data) == 0:
        return None
    maximum = data[0]
    for value in data[1:]:
        if value > maximum:
            maximum = value
    return maximum

# == OOP CLASS ==
class DataSet:
    def __init__(self, numerical_file=None, categorical_file=None):
        self.numerical_file = numerical_file
        self.categorical_file = categorical_file
        self.numerical_data = []
        self.categorical_data = []
        self.statistics = {}
        self.unique_categories = set()
    
    def load_data(self):
        """Load data from files with error handling"""
        # Load numerical data (Task 1 & 2)
        if self.numerical_file:
            try:
                # Check if file exists
                if not os.path.exists(self.numerical_file):
                    raise FileNotFoundError(f"File '{self.numerical_file}' not found")
                
                # Try to read as CSV first
                try:
                    with open(self.numerical_file, 'r') as file:
                        reader = csv.reader(file)
                        for row in reader:
                            if row:  # Skip empty rows
                                for item in row:
                                    try:
                                        # Try to convert to float
                                        value = float(item.strip())
                                        self.numerical_data.append(value)
                                    except ValueError:
                                        print(f"Warning: Non-numeric value '{item}' skipped")
                except:
                    # If CSV parsing fails, try reading as plain text
                    with open(self.numerical_file, 'r') as file:
                        content = file.read().strip()
                        if not content:
                            raise ValueError("File is empty")
                        
                        # Split by whitespace or commas
                        items = content.replace(',', ' ').split()
                        for item in items:
                            try:
                                value = float(item)
                                self.numerical_data.append(value)
                            except ValueError:
                                print(f"Warning: Non-numeric value '{item}' skipped")
                
                if len(self.numerical_data) == 0:
                    print("Warning: No valid numerical data found in file")
                    
            except FileNotFoundError as e:
                print(f"Error: {e}")
                self.numerical_data = []
            except Exception as e:
                print(f"Error reading numerical file: {e}")
                self.numerical_data = []
        
        # Load categorical data for sets (Task 6)
        if self.categorical_file:
            try:
                if not os.path.exists(self.categorical_file):
                    print(f"Warning: Categorical file '{self.categorical_file}' not found")
                    return
                
                with open(self.categorical_file, 'r') as file:
                    content = file.read().strip()
                    if not content:
                        print("Warning: Categorical file is empty")
                        return
                    
                    # Read categories (assuming one per line or comma-separated)
                    lines = content.split('\n')
                    for line in lines:
                        if ',' in line:
                            categories = [cat.strip() for cat in line.split(',') if cat.strip()]
                        else:
                            categories = [line.strip()]
                        
                        for category in categories:
                            if category:  # Skip empty strings
                                self.categorical_data.append(category)
                
                # Create set of unique categories
                self.unique_categories = set(self.categorical_data)
                
            except Exception as e:
                print(f"Error reading categorical file: {e}")
    
    def calculate_statistics(self, threshold=70):
        """Calculate all statistics and check performance"""
        # Calculate numerical statistics
        self.statistics['total'] = calculate_total(self.numerical_data)
        self.statistics['average'] = calculate_average(self.numerical_data)
        self.statistics['minimum'] = calculate_minimum(self.numerical_data)
        self.statistics['maximum'] = calculate_maximum(self.numerical_data)
        self.statistics['count'] = len(self.numerical_data)
        
        # Check performance (Task 5)
        if self.statistics['count'] > 0:
            if self.statistics['average'] > threshold:
                self.statistics['performance'] = "High Performance"
            else:
                self.statistics['performance'] = "Needs Improvement"
        else:
            self.statistics['performance'] = "No Data"
        
        # Calculate unique categories (Task 6)
        self.statistics['unique_categories'] = len(self.unique_categories)
        
        return self.statistics
    
    def display_results(self):
        """Display the calculated results"""
        print("\n" + "="*50)
        print("DATASET ANALYSIS RESULTS")
        print("="*50)
        
        if self.statistics['count'] > 0:
            print(f"\nNumerical Data Analysis:")
            print(f"  Total data points: {self.statistics['count']}")
            print(f"  Total: {self.statistics['total']:.2f}")
            print(f"  Average: {self.statistics['average']:.2f}")
            print(f"  Minimum: {self.statistics['minimum']:.2f}")
            print(f"  Maximum: {self.statistics['maximum']:.2f}")
            print(f"  Performance: {self.statistics['performance']}")
        else:
            print("\nNo numerical data available for analysis.")
        
        if self.unique_categories:
            print(f"\nCategorical Data Analysis:")
            print(f"  Unique categories: {self.statistics['unique_categories']}")
            print(f"  Categories: {', '.join(sorted(self.unique_categories))}")
        
        print("="*50)

# ==================== MAIN PROGRAM ====================
def save_report(statistics, unique_categories, filename="report.txt"):
    """Save results to a report file (Task 8)"""
    with open(filename, 'w') as file:
        file.write("DATASET ANALYSIS REPORT\n")
        file.write("="*40 + "\n\n")
        
        file.write("NUMERICAL STATISTICS:\n")
        file.write("-"*20 + "\n")
        if statistics['count'] > 0:
            file.write(f"Total data points: {statistics['count']}\n")
            file.write(f"Sum: {statistics['total']:.2f}\n")
            file.write(f"Average: {statistics['average']:.2f}\n")
            file.write(f"Minimum: {statistics['minimum']:.2f}\n")
            file.write(f"Maximum: {statistics['maximum']:.2f}\n")
            file.write(f"Performance Assessment: {statistics['performance']}\n")
        else:
            file.write("No numerical data available.\n")
        
        file.write("\nCATEGORICAL ANALYSIS:\n")
        file.write("-"*20 + "\n")
        if unique_categories:
            file.write(f"Number of unique categories: {len(unique_categories)}\n")
            file.write("Unique categories:\n")
            for category in sorted(unique_categories):
                file.write(f"  - {category}\n")
        else:
            file.write("No categorical data available.\n")
        
        file.write("\n" + "="*40 + "\n")
        file.write("Report generated successfully.\n")

def create_sample_files():
    """Create sample data files for testing"""
    # Create sample numerical data file
    with open('sample_data.csv', 'w') as f:
        f.write("85,92,78,88,95,67,74,89,91,82\n")
    
    # Create sample categorical data file
    with open('sample_categories.txt', 'w') as f:
        f.write("Math,Science,English,Math,History,Science,English,Art,Math,Science")

def main():
    """Main function to run the analysis"""
    # Create sample files (comment out if you have your own files)
    create_sample_files()
    
    print("Dataset Management and Basic Analysis System")
    print("-" * 40)
    
    # Get file names from user
    numerical_file = input("Enter numerical data filename (or press Enter for 'sample_data.csv'): ").strip()
    categorical_file = input("Enter categorical data filename (or press Enter for 'sample_categories.txt'): ").strip()
    
    # Use defaults if user doesn't specify
    if not numerical_file:
        numerical_file = "sample_data.csv"
    if not categorical_file:
        categorical_file = "sample_categories.txt"
    
    # Get performance threshold
    try:
        threshold = float(input("Enter performance threshold (default 70): ").strip() or "70")
    except ValueError:
        print("Invalid threshold. Using default value 70.")
        threshold = 70
    
    # Create DataSet object and run analysis (Task 7)
    dataset = DataSet(numerical_file, categorical_file)
    
    # Load data
    print("\nLoading data...")
    dataset.load_data()
    
    # Calculate statistics
    print("Calculating statistics...")
    statistics = dataset.calculate_statistics(threshold)
    
    # Display results
    dataset.display_results()
    
    # Save report to file (Task 8)
    report_file = input("\nEnter report filename (or press Enter for 'report.txt'): ").strip()
    if not report_file:
        report_file = "report.txt"
    
    save_report(statistics, dataset.unique_categories, report_file)
    print(f"\nReport saved to '{report_file}'")
    
    # Demonstrate individual functions (Task 3 & 4)
    if dataset.numerical_data:
        print("\n" + "-"*40)
        print("Demonstrating individual functions:")
        print(f"calculate_total result: {calculate_total(dataset.numerical_data):.2f}")
        print(f"calculate_average result: {calculate_average(dataset.numerical_data):.2f}")
        print(f"calculate_minimum result: {calculate_minimum(dataset.numerical_data):.2f}")
        print(f"calculate_maximum result: {calculate_maximum(dataset.numerical_data):.2f}")

if __name__ == "__main__":
    main()
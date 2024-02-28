#task04
#Magic square validator
def is_magic_square(matrix):
    # Check if matrix is 3x3
    if len(matrix) != 3 or any(len(row) != 3 for row in matrix):
        return False
    
    # Calculate the sum of the first row (the expected sum for a magic square)
    expected_sum = sum(matrix[0])
    
    # Check rows
    for row in matrix:
        if sum(row) != expected_sum:
            return False
    
    # Check columns
    for col in range(3):
        if sum(matrix[row][col] for row in range(3)) != expected_sum:
            return False
    
    # Check main diagonal
    if sum(matrix[i][i] for i in range(3)) != expected_sum:
        return False
    
    # Check secondary diagonal
    if sum(matrix[i][2 - i] for i in range(3)) != expected_sum:
        return False
    
    return True

def main():
    matrix = []
    print("Enter a 3x3 matrix (nine integer values):")
    for i in range(3):
        row = input().split()
        if len(row) != 3:
            print("Invalid input. Please enter exactly three values for each row.")
            return
        try:
            row = [int(num) for num in row]
            matrix.append(row)
        except ValueError:
            print("Invalid input. Please enter only integer values.")
            return
    
    if is_magic_square(matrix):
        print("The given matrix forms a magic square.")
    else:
        print("The given matrix does not form a magic square.")

if __name__ == "__main__":
    main()

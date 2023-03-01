"""maxAndMinEleInAnAraay.py
multiply a sqaure matrix with another square matrix 

loop one for row of an matrix
loop two for column of matrix
loop three for multiplying each element of loop one, two and placing it into another matrix 





"""
## talking about sqaure matrix where number of rows and cols are same
### If not then change 
## Taking the input for matrix 
def input_matrix(size_mat):
    row, col = size_mat,size_mat
    mat = []
    for i in range(size_mat):
        sample =[]
        for j in range(size_mat):
            ele = int(input("enter element"))
            sample.append(ele)
        mat.append(sample)
    return mat

def multiply(mat,size):
    result =[]
    for i in range(size):
        row = []
        for i in range(size):
            row.append(0)   
        result.append(row)
# multiplication

    for i in range(size):
        for j in range(size):
            for k in range(size):
                result[i][j] += mat[i][k]*mat[k][j]

    return result

if __name__ == "__main__": 
    mat =[[1,2,3],[4,5,6],[7,8,9]] 
    print(multiply(mat, 3))
import numpy as np

def transform(lst):
    '''Transforms 9-digit list into a 3x3 matrix.'''

    new_array = np.asarray([lst[0:3],
                            lst[3:6],
                            lst[6:]])
    
    return new_array



def matrix_mean(lst):
    
    '''Calculates the mean for all three columns and all three rows and then all total items in order specified by docstring.'''
    
    new = transform(lst)

    col1 = new[:,0].mean()
    col2 = new[:,1].mean()
    col3 = new[:,2].mean()

    row1 = new[0].mean()
    row2 = new[1].mean()
    row3 = new[2].mean()

    flat = new.mean()

    return [[col1, col2, col3], [row1, row2, row3], flat]



def matrix_variance(lst):

    '''Calculates the variance for all three columns and all three rows and then all total items.'''

    new = transform(lst)

    col1 = new[:,0].var()
    col2 = new[:,1].var()
    col3 = new[:,2].var()

    row1 = new[0].var()
    row2 = new[1].var()
    row3 = new[2].var()

    flat = new.var()

    return [[col1, col2, col3], [row1, row2, row3], flat]



def matrix_std(lst):

    '''Calculates the standard deviation for all three columns and all three rows and then all total items.'''

    new = transform(lst)

    col1 = new[:,0].std()
    col2 = new[:,1].std()
    col3 = new[:,2].std()

    row1 = new[0].std()
    row2 = new[1].std()
    row3 = new[2].std()

    flat = new.std()

    return [[col1, col2, col3], [row1, row2, row3], flat]



def matrix_max(lst):

    '''Finds the max for all three columns and all three rows and then all total items.'''

    new = transform(lst)

    col1 = new[:,0].max()
    col2 = new[:,1].max()
    col3 = new[:,2].max()

    row1 = new[0].max()
    row2 = new[1].max()
    row3 = new[2].max()

    flat = new.max()

    return [[col1, col2, col3], [row1, row2, row3], flat]



def matrix_min(lst):
    
    '''Finds the minimum for all three columns and all three rows and then all total items.'''

    new = transform(lst)

    col1 = new[:,0].min()
    col2 = new[:,1].min()
    col3 = new[:,2].min()

    row1 = new[0].min()
    row2 = new[1].min()
    row3 = new[2].min()

    flat = new.min()

    return [[col1, col2, col3], [row1, row2, row3], flat]



def matrix_sum(lst):

    '''Calculates the sum for all three columns and all three rows and then all total items.'''

    new = transform(lst)

    col1 = new[:,0].sum()
    col2 = new[:,1].sum()
    col3 = new[:,2].sum()

    row1 = new[0].sum()
    row2 = new[1].sum()
    row3 = new[2].sum()

    flat = new.sum()

    return [[col1, col2, col3], [row1, row2, row3], flat]



def calculate(lst):
    
    '''Records summary statistics of list turned into 3x3 matrix with the help of previous custom functions.'''

    dct = {
        'mean':matrix_mean(lst),
        'variance':matrix_variance(lst),
        'standard deviation':matrix_std(lst),
        'max':matrix_max(lst),
        'min':matrix_min(lst),
        'sum':matrix_sum(lst)
    }

    return dct
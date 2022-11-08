# For Python 2 / 3 compatability
from __future__ import print_function

training_data = [
    
     ['Red','Sports','Domestic','Yes'],
     ['Red','Sports','Domestic','No'],
     ['Red','Sports','Domestic','Yes'],
     
     ['Yellow','Sports','Domestic','No'],
     ['Yellow','Sports','Imported','Yes'],
    
     ['Yellow','SUV','Imported','No'],
     ['Yellow','SUV','Imported','Yes'],
     ['Yellow','SUV','Domestic','No'],
    
     ['Red','SUV','Imported','No'],
     ['Red','Sports','Imported','Yes'],
    
]




header = ["Color", "Type", "Origin","Stolen"]




def unique_vals(rows, col):
    """Find the unique values for a column in a dataset."""
    return set([row[col] for row in rows])



def class_counts(rows):
    """Counts the number of each type of example in a dataset."""
    counts = {}  # a dictionary of label -> count.
    for row in rows:
        # in our dataset format, the label is always the last column
        label = row[-1]
        if label not in counts:
            counts[label] = 0
        counts[label] += 1
    return counts



#######
# Demo:
class_counts(training_data)
#######



def is_numeric(value):
    """Test if a value is numeric."""
    return isinstance(value, int) or isinstance(value, float)
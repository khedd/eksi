"""
Annotation for annotating entries under categories.
To be used in ML tasks.
"""



def annotate_data(entries, targets):    
    labels = []
    print("Press q to quit")
    for entry in entries:
        print(' '.join(entry))
        target = input()
        if target == 'q':
            break
        labels.append(target)

    return labels


import os
#
class CommitDetail(object):
    def __init__(self, change_type, change_line):
        self.change_type = change_type
        self.change_line = change_line
        
        
class CommitHeader(object):
    def __init__(self, revision = None, author = None, date = None, commentLineCount = None, day = None):
        self.Revision = revision
        self.Author = author
        self.DateTime = date
        self.DayOfWeek = day
        self.CommentLineCount = commentLineCount
        self.Changes = []
        self.Comment = []
        self.NoOfChanges = 0


def load_data(filename):
    data = [line.strip() for line in open(filename, "r")]
    return data

def return_no_of_commits(data, author = None):
    found = 0
    if author == None:
        return len(data)
    for idx in range(0, len(data)):
        if author in data[idx].Author:
            found = found + 1
    return found
    
def return_no_of_change_types(data, change_type = None, author = None):
    idx_change = 0
    found = 0
    for idx in range(0, len(data)):
        for idx_change in range(0, len(data[idx].Changes)):
            if data[idx].Changes[idx_change].change_type == change_type or change_type == None:
                if author == None or author in data[idx].Author:
                    found = found + 1
    return found
    
def CreateMatrix(data):
    sep = 72 * '-'
    idx = 0
    NewCommitFile = []

    while idx < len(data) - 1:
        if data[idx] == sep:
            #
            #    If Separator then next line is header - Fill in HeaderDetails
            #
            HeaderDetails = data[idx + 1].split('|')
            NewCommitHeader = CommitHeader(HeaderDetails[0], HeaderDetails[1], HeaderDetails[2], HeaderDetails[3])
            #   Now extract day of week from header
            i1 = (NewCommitHeader.DateTime.find("(") + 1)
            i2 =  NewCommitHeader.DateTime.find(",", (NewCommitHeader.DateTime.find("(") + 1))
            NewCommitHeader.DayOfWeek = (NewCommitHeader.DateTime[i1:i2])
            #
            #    Loop through path changes and add into CommitChange object
            for idx in range(idx+3,data.index('', idx + 3)):
                CommitDetails = data[idx].split(' ')
                NewCommitDetail = CommitDetail(CommitDetails[0], CommitDetails[1])
                NewCommitHeader.Changes.append(NewCommitDetail)
                NewCommitHeader.NoOfChanges =    NewCommitHeader.NoOfChanges + 1
            for i in range(idx+2,data.index(sep, idx)):
                if data[i] <> "" and data[i] <> None:
                    NewCommitHeader.Comment.append(data[i])
            NewCommitFile.append(NewCommitHeader)
        idx = idx + 1
    return NewCommitFile

def return_comments(data, revision):
    for f in data:  
        if revision in f.Revision:
            print f.Revision, " ", f.Comment
            return len(f.Comment)
    return -1
            
            
def display_results_by_author():
    FullData.sort(key = lambda i: (i.Author).lower())
    print(" Author                                               Commits   Del   Add   Mod  Read     Total")
    print("--------------------------------------------------    -------   ---   ---   ---  ----     -----")
    prev_Author = " "
    
    for f in FullData:
        if f.Author <> prev_Author:
            print("{:50} {:10} {:5} {:5} {:5} {:5} {:9}").format(f.Author, return_no_of_commits(FullData, f.Author), return_no_of_change_types(FullData, "D", f.Author), return_no_of_change_types(FullData, "A", f.Author), return_no_of_change_types(FullData, "M", f.Author), return_no_of_change_types(FullData, "A", f.Author), return_no_of_change_types(FullData, None, f.Author))
            prev_Author = f.Author
    print("--------------------------------------------------    -------   ---   ---   ---  ----     -----")
    print("{:50} {:10} {:5} {:5} {:5} {:5} {:9}").format("Total", return_no_of_commits(FullData), return_no_of_change_types(FullData, "D"), return_no_of_change_types(FullData, "A"), return_no_of_change_types(FullData, "M"), return_no_of_change_types(FullData, "R"), return_no_of_change_types(FullData))

def display_results_by_day():
    FullData.sort(key = lambda i: (i.DayOfWeek).lower())
    print(" Day                                                  Commits   Del   Add   Mod  Read     Total")
    print("--------------------------------------------------    -------   ---   ---   ---  ----     -----")
    prev_DayOfWeek = None
    total_commits = 0
    total_del = 0
    total_add = 0
    total_read = 0
    total_mod = 0
    
    for f in FullData:
        if f.DayOfWeek <> prev_DayOfWeek:
            if prev_DayOfWeek <> None:
                print("{:50} {:10} {:5} {:5} {:5} {:5} {:9}").format(prev_DayOfWeek, total_commits, total_del, total_add, total_mod, total_read, (total_del + total_add + total_mod + total_read))
                total_commits = 0
                total_add = 0
                total_del = 0
                total_read = 0
                total_mod = 0
            prev_DayOfWeek = f.DayOfWeek
        total_commits = total_commits + 1
        for g in f.Changes:
            if g.change_type == "D":
                total_del = total_del + 1
            elif g.change_type == "M":
                total_mod = total_mod + 1
            elif g.change_type == "A":
                total_add = total_add + 1
            elif g.change_type == "R":
                total_read = total_read + 1
            else:
                print "No such change type catered for - ", g.change_type
    print("--------------------------------------------------    -------   ---   ---   ---  ----     -----")
    print("{:50} {:10} {:5} {:5} {:5} {:5} {:9}").format("Total", return_no_of_commits(FullData), return_no_of_change_types(FullData, "D"), return_no_of_change_types(FullData, "A"), return_no_of_change_types(FullData, "M"), return_no_of_change_types(FullData, "R"), return_no_of_change_types(FullData))

    
if __name__ == "__main__":
    os.system('cls')
    data = load_data("changes_python.log")
    FullData = CreateMatrix(data)
    display_results_by_author()
    print("\n\n")
    display_results_by_day()
    print(return_comments(FullData, "r1540809"))
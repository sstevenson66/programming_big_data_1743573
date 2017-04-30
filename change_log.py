#  Commit has Revison Number, Name, Date etc
#
class CommitDetail(object):
	def __init__(self, change_type, change_line):
		self.change_type = change_type
		self.change_line = change_line
		
		
class CommitHeader(object):
	def __init__(self, revision = None, author = None, date = None, commentLineCount = None, day = None,
			comment = None):
		self.Revision = revision
		self.Author = author
		self.DateTime = date
		self.DayOfWeek = day
		self.CommentLineCount = commentLineCount
		self.Changes = []
		self.Comment = comment
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
    
def return_no_of_change_types(data, change_type, author = None):
	idx_change = 0
	found = 0
	for idx in range(0, len(data) - 1):
		for idx_change in range(0, len(data[idx].Changes) - 1):
			if data[idx].Changes[idx_change].change_type == change_type:
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
			#	If Separator then next line is header - Fill in HeaderDetails
			#
			HeaderDetails = data[idx + 1].split('|')
			NewCommitHeader = CommitHeader(HeaderDetails[0], HeaderDetails[1], HeaderDetails[2], HeaderDetails[3])
                        print(NewCommitHeader.Author)
			i1 = (NewCommitHeader.DateTime.find("(") + 1)
			i2 =  NewCommitHeader.DateTime.find(",", (NewCommitHeader.DateTime.find("(") + 1))
			NewCommitHeader.DayOfWeek = (NewCommitHeader.DateTime[i1:i2])
			#
			#	Loop through path changes and add into CommitChange object
			#
			for idx in range(idx+3,data.index('', idx + 3)):
				CommitDetails = data[idx].split(' ')
				NewCommitDetail = CommitDetail(CommitDetails[0], CommitDetails[1])
				NewCommitHeader.Changes.append(NewCommitDetail)
				NewCommitHeader.NoOfChanges =	NewCommitHeader.NoOfChanges + 1
			NewCommitFile.append(NewCommitHeader)
			###print "idx = ", idx, "next is ", data.index(sep, idx + 1), " NewCommitFile length = ", len(NewCommitFile)
		idx = idx + 1
	return NewCommitFile

	
if __name__ == "__main__":
    data = load_data("changes_python.log")
    FullData = CreateMatrix(data)
    print(return_no_of_commits(FullData, "Vincent"))
    
    print FullData[0].Author, " 0"
    FullData.sort(key = lambda i: (i.Author).lower())
    print(return_no_of_commits(FullData))
    print(" Author                                               Commits   Del   Add   Mod")
    print("--------------------------------------------------    -------   ---   ---   ---")
    prev_Author = " "
    for f in FullData:
        if f.Author <> prev_Author:
            print("{:50} {:10} {:5} {:5} {:5}").format(f.Author, return_no_of_commits(FullData, f.Author), return_no_of_change_types(FullData, "D", f.Author), return_no_of_change_types(FullData, "A", f.Author), return_no_of_change_types(FullData, "M", f.Author))
            prev_Author = f.Author
    print "____"
    #print(return_no_of_commits(FullData))
    #print(return_no_of_commits(FullData, "Thomas"))
    print(return_no_of_change_types(FullData, "D"))
    print(return_no_of_change_types(FullData, "A"))
    print(return_no_of_change_types(FullData, "M"))
    print(return_no_of_change_types(FullData, "D", "Thomas"))
	
    
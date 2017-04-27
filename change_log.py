#  Commit has Revison Number, Name, Date etc
#


class CommitDetail(object):
	def __init__(self, change_type, change_line):
		self.change_type = change_type
		self.change_line = change_line
		
		
class CommitHeader(object):
	def __init__(self, revision = None, author = None, date = None, commentLineCount = None, 
			comment = None):
		self.Revision = revision
		self.Author = author
		self.DateTime = date
		self.CommentLineCount = commentLineCount
		self.Changes = []
		self.Comment = comment
		self.NoOfChanges = 0


def load_data(filename):
	data = [line.strip() for line in open(filename, "r")]
	return data

	
def CreateMatrix(data):
	sep = 72 * '-'
	idx = 0
	NewCommitFile = []

	while idx < len(data) - 1:
		if data[idx] == sep:
			HeaderDetails = data[idx + 1].split('|')
			NewCommitHeader = CommitHeader(HeaderDetails[0], HeaderDetails[1], HeaderDetails[2], HeaderDetails[3])
			for idx in range(idx+3,data.index('', idx + 3)):
			#
			#	Loop through path changes and add into CommitChange object
			#
				CommitDetails = data[idx].split(' ')
				NewCommitDetail = CommitDetail(CommitDetails[0], CommitDetails[1])
				NewCommitHeader.Changes.append(NewCommitDetail)
				NewCommitHeader.NoOfChanges =	NewCommitHeader.NoOfChanges + 1
			#print len(HeaderDetails)
			NewCommitFile.append(NewCommitHeader)
			print "idx = ", idx, "next is ", data.index(sep, idx + 1), " NewCommitFile length = ", len(NewCommitFile)
		idx = idx + 1
	return NewCommitFile


	
if __name__ == "__main__":
	data = load_data("changes_python.log")
	FullData = CreateMatrix(data)
	print len(FullData)



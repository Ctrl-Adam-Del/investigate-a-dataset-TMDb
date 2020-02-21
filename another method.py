'''This is another way to create a funtion that create DataFrames and split specific column by '|' '''
multigenres = df[df['genres'].str.contains('\|')]
multigenres
# looks like one movie can have upto four genres
# so we make four copies
# create function
# Function to create DataFrames and split specific column by '|'
def split_genres(DataFrameDict, DataFrameToCopy, CopyCount, SplitField, SplitIndex):
  if CopyCount != len(SplitIndex):
    return ('CopyCount does not match SplitIndex count/length!')
  for i in np.arange(CopyCount):
    DataFrameDict['df'+str(i+1)] = DataFrameToCopy.copy()
    DataFrameDict['df'+str(i+1)][SplitField] = DataFrameDict['df'+str(i+1)][SplitField].apply(lambda x : x.split('|')[SplitIndex[i]])
#Execute Function
dataFrameList = {} # this is needed to create a dictionary of DataFrames
# call split_genres function
split_genres(dataFrameList, multigenres, 4, 'genres', [0, 1, -2, -1])
# Display DataFrame(s) from Dictionary
# With CopyCount = 4, DataFrames df1, df2, df3, and df4 created. They can be accessed via the following
dataFrameList['df2']
# append four dataframes together then drop duplicates
new_rows = dataFrameList['df1'].append(dataFrameList['df2'].append(dataFrameList['df3'].append(dataFrameList['df4'])))
new_rows.drop_duplicates(inplace= True)

# Twitter Embeddings Analysis

https://arxiv.org/abs/1703.00607

## Project Goals:

**Unrelated Tasks:**
 - Remove or move all files that are not being used
 - Background research to compile for intro portion of manuscript

**Preprocessing Milestone:**
 - Code that reads .json file, processes the tweets by removing hashtags, usernames, rt's, and common stop words, and separates them into dictionaries by week or month(36 weeks total, 8 months) 2018-10-22 is the start 2018-09-20 is the end
   - The dictionaries can be saved as text files as long as there is a character that separates all of the tweets
 - Code that gets the word counts for each word then saves it in a data frame,
   - Check for empty values before we save the data frames
   - Name should look like "wc_2018-10-22.csv" or something like it
 - Code that gets the window count of the words and saves them to a data frame
   - Also organized by time and named accordingly like "wnd_2018-10-22.csv" or something like that
   - Also check for empty entries
   - We should be able to adjust the window length
 
**Construct PPMI - mostly finished**
 - Code must read word count and window count data frames
   - Code must create V a dictionary of all vocabulary from all time segments
 - Code must create PPMI’s for all time segments
 - The matrix is V x V where V is the length of the overall vocabulary
 - Code must calculate the PPMI value and create the PPMI matrix
 - Testing
   - Test the accuracy of the embeddings through simple comparison test 
     - Ex: queen - woman + man = king
 
**Align PPMIs:**
 - Implement model from DWEESD paper
   - Y(t) is the PPMI matrix for a time t
   - U(t) is the temporal embedding
   - This part will need a factorization method for getting the vectors U(t)
   - We need to use numpy or scipy to be able to create U(t)U(t)T
 - Finding ideal lambda and rau values
   - ƛ > 0 they used 10
   - 𝜏 > 0 they used 50
   - We will have to test a range of numbers

**Paper:**
 - Write introduction
 - Write Abstract
 - ...

## Project Members:

**Kevin Sadi:** Developing data preprocessing script.

**Zane Page (Project Lead):** Implementing algorithm for PPMI matrices.

**Ivan Mo:** Updating project description files and following along with Kevin's work.

**Krishi Kishore:** Working on algorithm for alignment of PPMI matrices across time.

## Sources:

**Dynamic Word Embeddings for Evolving Semantic Discovery:**
https://arxiv.org/abs/1703.00607

~~This file needs more information about the project: who is working on it, what they're working on, the goals of the project, how to get started, and where the project currently stands.~~

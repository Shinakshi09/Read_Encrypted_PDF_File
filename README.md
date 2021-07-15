# Reading-pdf-files-and-converting-to-machine-readable-formats-using-python
**Problem Statement**

Users have pdf files which contains investment details of a particular user.Since this data is contained inside pdf format, we need to convert it into machine readable format i.e into dataframes.

**Business perspective**

Once we have pdf data in machine readable format, we can perform further computations on the user’s particular portfolio. For example: calculating portfolio beta, standard deviation, etc. and the user can have an overall summary about his portfolio in one go. 

**Process**

I went through many approaches in order to solve this problem. Let's discuss them

Firstly I researched what all python libraries we can use in order to read pdf files. I came across a few of the names such as camelot, pypdf2, pdfplumber, tabula etc…

I started with camelot as camelot extracts tables as it is from the pdf files. In order to do that, camelot required its dependencies to be installed which were ghostscript and tkinter. When the installation was complete and I tried to read the pdf file, it was extracting only 1 table. Remember table means bounded part or which has all the four boundaries. That's why it didn’t extract the input pdf file data. One disadvantage of camelot is that it works with ASCII passwords only or no password at all. (ASCII means should contain at least one of the special characters)

Tried extracting data using tabula but again tabula also extracts tables from the pdf file. So this approach was also cancelled.

Read the pdf file using PYPDF2 and decrypt also as we were dealing with encrypted files. It read the data but couldn't perform further steps. 

Finally PDFPLUMBER came into picture which read the data correctly and decrypt also. Earlier page was being split while reading the pdf file. This was because in the end of the page , to the bottom rightmost corner, few alphabets were written there as shown below which got resolved using parameter y_tolerance=1 inside extract_text pdf_page.extract_text(y_tolerance=1)

Now to get the desired data frame format, I have used regex expressions for the predefined columns so that matched data should go inside that particular column.

**Logic applied**

Firstly defining all the columns to be created using namedtuple. 

Logic was applying regex expression in order to find the records which were starting with a particular scheme code (such as 112JHGPG) followed by its name and other things ie company_re and there were few schemes such as F-17, K103 where alphabets were coming before digits so we applied one more regex naming schemes_re. Similarly schemes_re_1 and num were also defined for various combination of schemes name (ie it might be combination of all digits, all alphabets, combo of both etc)

Then for above regex expressions i.e. for a particular scheme code, whole transactions under that code should reflect in the dataframe. That's why we defined one more regex naming line_re which is extracting date, transaction, amount, units, price and unit_balance.

Taking an empty list and applying for loop over all the text data which was read using the library and searching for the above regex expression results in the text file. 

Apply if else statement now in order to fill columns with its matched regex values. 

Append this namedtuple inside the empty list and convert this list into dataframe. 


**Dataset** 
File contains pages like following:
![z](https://user-images.githubusercontent.com/87409887/125751467-e14ab795-c62a-4827-b680-b5ff3888641c.PNG)


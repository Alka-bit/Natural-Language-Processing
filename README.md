# Natural-Language-Processing

#Type and Token 
 
In the study of texts; the ratio of the number of different words, called types while the total number of words in a certain text is called token.The distinction between a type and its tokens is a useful metaphysical distinction. Type is considered to be concept and takens are instances of concept

Will will will -----> { Type = 1, Token = 3
                                (Unique words) (Total number of words)  
 
Type-Token distinction 

The distinction between a type and its tokens is an ontological one between a general sort of thing and its particular concrete instances (to put it in an intuitive and preliminary way).  The type–token distinction is the difference between naming a class (type) of objects and naming the individual instances (tokens) of that class. 

Type/Token Ratio

The type/token ratio (TTR) is the ratio of the number of different words(types) to the number of running words(tokens) in a given text. This index indicates how often, on average, a new ‘word form’ appears in the text or corpus.

Case : Mark Twain’s Tom Sawyer 
Tokens : 71370
Type : 8018
TTR : Type/Token = 8010/71370 = 0.112

Complete Shakespeare work 
Token : 884647
Type : 29066
TTR : 0.032

High TTR → Tendency to use new words
Low TTR → Tendency to use less new words (repetition of words)

Comparing Conversations, Academics, News, Fiction
Conversations → Lowest TTR … as we tend to repeat words in normal conversation
Fiction → Low TTR
Academic → High
News → Highest 

News > Academic > Fiction > Conversations 

**TTR in not a valid measure of text complexity as the values varies with size of the text and for valid measure, a running average is computed on consecutive 1000-words chucks of the text.

Consider a text, containing 60000 tokens. The TTR for the first 30000 tokens is equal to  r30K and for other 30000 tokens is r60K. Therefore, we can imply that r60K >r30K. Since most of the words are considered to be covered in the first 30000 tokens.


  

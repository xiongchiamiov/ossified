People get confused about software licenses all the time, and often end up
choosing one based on faulty reasoning.  While I'm not an expert on licensing
(IANAL and all that), I've read the common licenses multiple times and spend
all too much time debating their respective merits.  So, I thought I'd make a
tool to help people.

However, my desire to play around with [Ren'Py] was rekindled by [Analogue: A
Hate Story].  So, since my drawing skills are... rudimentary, I downloaded a
few images of [Wikipe-tan] and set off on my way.

# The Name

Oh yeah, the name... You see, we're talking about *O*pen-*S*ource *S*oftware,
so you might say we're *oss*ifying a project... yeah.

# Installation

1. [Download Ren'Py](http://www.renpy.org/latest.html).
2. Extract the downloaded file.
3. [Download ossified](https://github.com/xiongchiamiov/ossified/archive/master.zip).
4. Extract it into the Ren'Py folder.
5. Run Ren'Py, select "ossified-master" in the project list, and hit "Launch
   Project".

# The Licenses

Here are the licenses Ossified will point you at; the preference is for common
licenses, and only one for each category.

 -------------------------------------------------------------------------------
| License      | Copyleft? | State changes?  | Attribution? | Must change name? |
|--------------|-----------|-----------------|--------------|-------------------|
| GPLv3        |     x     |       x         |      x       |                   |
| LGPL         |     x     |       x         |      x       |                   |
| AGPL         |     x     |       x         |      x       |                   |
| Apache       |           |       x         |      x       |         x         |
| Zlib         |           |                 |      x       |         x         |
| BSD 3-clause |           |                 |      x       |         x         |
| MIT          |           |                 |      x       |                   |
| WTFPL        |           |                 |              |                   |
 -------------------------------------------------------------------------------

The difference between the Zlib and BSD 3-clause licenses is subtle - Zlib
requires you to change the name of the project if you make any modifications,
while the BSD license only requires that you not use any names of contributors
to promote your new version.

[Ren'Py]: http://www.renpy.org/
[Analogue: A Hate Story]: http://ahatestory.com/
[Wikipe-tan]: http://en.wikipedia.org/wiki/Wikipedia:Wikipe-tan


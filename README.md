Summary

I combine the PISA 2012 data with GDP to explore the correlation between family possession and scores, and how GDP per capita affect the correlation.

Design

PISA collects information how many car, cellphone, TV, computer and bathroom students have. For each country, I make a box plot of score for every factor. They show some interesting correlation. The increasing possession of some factors helps students' scores while some hurts. Countries are categorized by their GDP per capita and the type of correlations are summarized in a multiple line chart. Finally, an interactive map is presented for user to explore.
The choice of colors: 
I made the line charts in slide 4-6 first because they could be done with dimple.js. The color scheme was decided by dimple and I found it nice. As the result, I kept the scheme in box plots to make things consistent. I know there are some theories about color using, but here as it only needed three colors, so I chose from intuition. 
The color of legend of GDP per capita was decided as follows, usually bad things (e.g., being a poor country) are presented by red/yellow, while good things by blue/purple. I observed that most countries have GDP per capita fewer than $100000, so I found a scale from red to purple with 10 classes on colorbrewer2.org.
The choice of graph types: 
I chose box plots instead of scatter plots or line charts of mean values to present the scores, because box plots convey more information. PISA is a really large dataset. It would be waste mean values. Box plots show information like the distribution of scores that other plots don't. Such information might be analyzed further, for example, related to Gini coefficients of countries. 
I chose line charts rather than more usual bar charts because bar charts get messy easily here. My purpose was to compare the type of correlation for various type of countries. The stacked bar charts would be hard for comparison, while to compare in dodged bars, one's eyes have to skip two other types of country to find the next point of the same type. I believe the current line charts are the best choice.
For the countries chosen in slide 2 and 3, they were chose a bit arbitrarily. Many low-income countries show the same effect, but Peru and Vietnam were the ones I found first, so I used them. USA was chose because we all care about it. Switzerland was chose because I was looking for a even richer country with high social welfare and fewer immigrants.


Feedback

I got three comments.
1. There was a bug in the first page. If one clicks to the "technical detail" page and comes back, the page didn't load correctly;
2. Add navigation to every page;
3. Use a prettier font.
I've improved the page accordingly. Checkout the oldest commits to see the initial version. The GitHub link is https://github.com/tcya/PISA_visualization.

Resources

https://gist.github.com/markmarkoh/2969317
https://www.kaggle.com/c/acquire-valued-shoppers-challenge/forums/t/7883/r-fread-for-large-files/71396
https://discussions.udacity.com/t/question-to-dataset-pisa/21365
https://stackoverflow.com/questions/9520840/using-regexp-to-select-rows-in-r-dataframe
https://cran.rstudio.com/web/packages/dplyr/vignettes/introduction.html
https://stackoverflow.com/questions/14096814/r-merging-a-lot-of-data-frames
https://stackoverflow.com/questions/17108191/how-to-export-proper-tsv
http://bl.ocks.org/mbostock/4061502
https://cran.r-project.org/web/packages/dplyr/vignettes/nse.html
https://github.com/hadley/dplyr/issues/906
https://stackoverflow.com/questions/27197617/filter-data-frame-by-character-column-name-in-dplyr
https://cran.r-project.org/web/packages/rjson/rjson.pdf
https://stackoverflow.com/questions/9589768/using-an-associative-array-as-data-for-d3
http://bl.ocks.org/mbostock/3886208
https://github.com/mbostock/d3/wiki/Ordinal-Scales
https://stackoverflow.com/questions/15580300/proper-way-to-draw-gridlines
https://stackoverflow.com/questions/11189284/d3-axis-labeling
http://bl.ocks.org/phoebebright/3061203
https://stackoverflow.com/questions/17791926/how-to-rotate-x-axis-text-in-dimple-js
https://stackoverflow.com/questions/25416063/title-for-charts-and-axes-in-dimple-js-charts
https://stackoverflow.com/questions/11488194/how-to-use-d3-min-and-d3-max-within-a-d3-json-command
https://github.com/mbostock/d3/wiki/Quantitative-Scales#linear_domain
https://stackoverflow.com/questions/17406855/d3-js-restore-previous-color-on-mouseout
http://colorbrewer2.org/
https://stackoverflow.com/questions/8543859/css-vertical-alignment-text-inside-li
http://mikemcdearmon.com/portfolio/techposts/fun-with-d3-maps
https://stackoverflow.com/questions/10805184/d3-show-data-on-mouseover-of-circle
http://bl.ocks.org/mbostock/eec4a6cda2f573574a11
http://techslides.com/demos/d3/worldmap-template.html
http://bl.ocks.org/mbostock/3711652
https://stackoverflow.com/questions/2580772/how-do-i-get-a-new-line-after-using-floatleft

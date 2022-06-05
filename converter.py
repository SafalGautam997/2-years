import pandas
file = pandas.read_csv("PewdiepieSubmissions_comments_FELIX AND MARZIAsubreddit.csv")
fle = pandas.read_csv("PewdiepieSubmissions_FELIX AND MARZIAsubreddit.csv")
file.to_html("Comments.html")
fle.to_html("Main.html")
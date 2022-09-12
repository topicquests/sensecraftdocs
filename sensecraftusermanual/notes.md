## Design notes
There is an intention to create this manual as if it was an IBIS structured conversation, where nodes in that conversation are individual html files.

I am thinking about experimenting with the CSS layout tool https://griddy.io/ to create a few templates; each node will follow the patterns of just a very few different templates.

### Node design
- Each node may or may not have a link to a *parent* node; together with a tiny icon reflecting the node type to which the link points
- Each node may or may not have one or more links to *child* nodes; together with a tiny icon reflecting the node type to which the link points
- Each will have a title, which is one of a Question, Answer, Pro or Con Argument, or Reference; each such title will include a small icon which matches the node type
- Each node may or may not have a body of rich text which adds details related to the title text - say, a left side column
- Each node may or may not have a graphic illustration, say, a right side column






from app import db
from app.models import Post, Country


postlist = Post.query.filter_by(approved=False).all()
countlist = Country.query.filter_by(approved=False).all()

for i in postlist:
	i.approved = True

for j in countlist:
	j.approved = True

db.session.commit()
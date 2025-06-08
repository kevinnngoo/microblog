from typing import Optional
from datetime import datetime, timezone
import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db

#goal: make a table named users with an id column that is an integer and is the primary key

class User(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    username: so.Mapped[str] = so.mapped_column(sa.String(64), unique=True, nullable=False)
    email: so.Mapped[Optional[str]] = so.mapped_column(sa.String(120), unique=True, nullable=True)
    password_hash: so.Mapped[str] = so.mapped_column(sa.String(256), nullable=False)

    posts: so.WriteOnlyMapped["Post"] = so.relationship(back_populates="author", cascade="all, delete-orphan")

    def __repr__(self):
        return f'<User {self.username}>'
    

#id integer, primary key
#body varchar(140)
#timestamp datetime
#user_id integer

class Post(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    body: so.Mapped[str] = so.mapped_column(sa.String(140))
    timestamp: so.Mapped[datetime] = so.mapped_column(sa.DateTime, index=True, default=lambda: datetime.now(timezone.utc))
    user_id: so.Mapped[int] = so.mapped_column(sa.ForeignKey('user.id'))

    author: so.Mapped["User"] = so.relationship('User', back_populates='posts')

    def __repr__(self):
        return '<Post {}>'.format(self.body)
# Insta API

A RESTful API for simple Instagram-like application.

API was created using Python language, Django and Django REST Framework. API Documentation is made with Swagger.

Authenticated user can perform actions such as adding post, adding comment, following other user, view posts, likes, comments etc. All that by connecting with different endpoints.

Project uses default Django database at the moment (SQLite).

## API
### /photos
‌* GET : Get all photos
‌* POST : Create new photo
### /photos/:photo_id
‌* GET : Get photo with given photo_id
‌* PUT : Update photo with given photo_id
‌* DELETE : Delete photo with given photo_id
### /photos/:photo_id/comments
‌* GET : Get comments under photo with given photo_id
‌* POST : Create new comment under photo with given photo_id
### /photos/:photo_id/likes
‌* GET : Get likes under photo with given photo_id
‌* POST : Create like under photo with given photo_id
### /comments/:comment_id
‌* GET : Get comment with given comment_id
‌* PUT : Update comment with given comment_id
‌* DELETE : Delete comment with given comment_id
### /likes/:like_id
‌* DELETE : Delete like with given like_id
### /users/:following_id/followers
‌* GET : Get all followers of user with given following_id
‌* POST : Follow user with given following_id
### /follows/:follow_id
‌* DELETE : Delete follow with given follow_id

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)

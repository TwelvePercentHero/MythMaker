# MythMakers - Full Stack Frameworks Milestone Project

[![Build Status](https://travis-ci.org/TwelvePercentHero/MythMaker.svg?branch=master)](https://travis-ci.org/TwelvePercentHero/MythMaker)

MythMakers is an online storytelling community designed to help creative people tell interesting stories in a variety of online-accessible media including written prose, videos and audio. They can also like and comment on different stories to add them to their own personal feed of media, and edit their own profile to create a personalised space on the site. There is also a paid subscription option, for a charge of £5 per month the user is able to upgrade, allowing them to upload video and audio stories as well as written stories, which are available for upload by all users.

## UX

My goal in the design and development of the website was to create a site which was easy to navigate, taking into consideration the large number of different file types stored on the site. It was also important for the user to be able to personalise their own space on the website in an effort to promote the community aspect, where each person has access to the same space and tools but is able to display it in a different way.

I looked at a number of existing online communities including [https://roosterteeth.com/](https://roosterteeth.com/) and [https://sorted.club/](https://sorted.club) for inspiration in the design, development and business model of similar websites, and noticed that there was generally a free user tier and a paid subscription model, and I decided to adopt this pattern for the MythMakers site.

The user accounts aspect of the site was the most important and the one I wanted to focus on in initial stages of development so I built mockups which can be found in the doc folder to give a visual representation of how I wanted the pages to come together. The registration and login experience needed to be simple and seamless, and utilising the built-in functionality of the Django framework was vital in allowing me to do this. However I wanted to customise the experience with the addition of clear and well-formatted emails sent to the user, so added HTML email templates into the process to help guide the user through the registration and login process.

I also wanted the user to have a profile through which they could perform a variety of actions, including browsing and storing their own uploaded and liked stories, and updating their own personal information.

Beyond the user accounts section of the website, I wanted the information in the stories to be clear and appropriate to the type of media which was being used. As such a different layout was required for each of the three main media types: stories (written prose), videos and audio.

The stories pages were the simplest to lay out as I knew that the text needed to be the main element on the page and everything else was secondary, so I ensured that the user was able to upload their stories in HTML format to ensure that they could be spaced out and formatted suitably.

For the video app I looked at sites such as YouTube and Vimeo for inspiration around how to lay out the video and videolist pages of the site in a user-friendly and easy to navigate way. A combination of Google Developer Tools and the web tool [VisBug](https://chrome.google.com/webstore/detail/visbug/cdockenadnadldjbbgcallicgledbeoc) was invaluable in looking at the way popular video streaming sites are laid out both in a desktop browser and on a mobile device.

With the design of both the stories and videos pages in place, I repurposed elements of each for the audio pages - these posed some challenges as the audio players took up far less space on the page than either the story text or the video player, so reformatting the layout to better suit the contents was important.

Overall responsive design was a vital part of the development process and I wanted to ensure that the user had a similar experience regardless of what device they were using. To this end I decided that Bootstrap v4 was an ideal tool to help me build the design of the website as the column layout was easy to develop for a range of devices.

## Technologies

- [Python3](https://www.python.org)
  - I used Python3 to develop all backend code and functions.
- [Django v2.2](https://www.djangoproject.com/start/overview/)
  - I used the Django framework extensively to help me build and develop the structure of the website as well as the various views, URLs, models and forms included within the site. I also used Django's built-in testing framework to test my code.
- [PostgreSQL](https://www.postgresql.org/)
  - I used a PostgreSQL database to store and retrieve the data for the various apps included within the website as it was a robust data store that worked well with Heroku for deployment purposes.
- [PgAdmin 4](https://www.pgadmin.org/)
  - PgAdmin was a useful took for navigating and understanding the PostgreSQL database that I had built as part of the project.
- [Stripe](https://stripe.com/gb)
  - Stripe was used to manage payments and subscriptions to the website through a secure service.
- [Pillow](https://pillow.readthedocs.io/en/stable/)
  - As images were in heavy use across the site, Pillow was necessary to manage the image files and types.
- [TinyMCE](https://www.tiny.cloud/)
  - For the upload function in the stories app I wanted to provide a rich-text HTML option for uploading the story, and found TinyMCE a simple and effective tool for doing this.
- [Jinja](http://jinja.pocoo.org)
  - I used Jinja2 to effectively display data from the backend database in HTML on the frontend.
- [HTML5](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5)
  - The project uses HTML5 for the overall structure and content of the website.
- [CSS3](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS3)
  - The project uses CSS3 for the style and format of the website.
- [Bootstrap v4.3.1](https://getbootstrap.com/docs/4.3/getting-started/introduction/)
  - The project uses Bootstrap v4.3.1 for additional style and format options, including the grid system and mobile responsive elements. The Bootstrap jQuery script has also been included in the site to facilitate the modal popup windows.
- [jQuery](https://jquery.com/)
  - jQuery was used in the project to handle certain transitions, particularly the show/hide functions on the different tabs of story results.
- [Google Fonts - Questrial](https://fonts.google.com/specimen/Questrial)
  - Questrial was used as the font throughout the website due to its clean appearance and ubiquity through Google Fonts.
- [Visbug](https://chrome.google.com/webstore/detail/visbug/cdockenadnadldjbbgcallicgledbeoc)
  - I used Visbug in the design and development stages of the project to understand the layout of existing websites and build a similar design for this one.
- [Balsamiq](https://balsamiq.com/)
  - Balsamiq was used for building wireframes in the early development stages of the project.
- [Google Chrome Developer Tools](https://developers.google.com/web/tools/chrome-devtools)
  - I used Google Chrome Developer Tools consistently through the development of the project to ensure the site was responsive and displayed effectively across a range of devices.
- [Travis Continuous Integration](https://travis-ci.org/)
  - As part of the automated testing for the site I used Travis to continually test the build of my code.
- [Microsoft Visual Studio Code](https://code.visualstudio.com/)
  - The project was built entirely in VSCode as I found it was a robust IDE that was able to handle the large number of apps and modules the project contained.
- [Adobe Photoshop](https://www.photoshop.com/)
  - I edited a number of images to be displayed on the site, including the background image, header images and thumbnails, as well as the main icon and logo for MythMakers.

## Features

As the scope of this project was considerable, I chose to treat it in development terms as a minimum viable product (MVP) with the key features and functions being the primary concern. As such, there were a number of features which were left as future development priorities.

### Existing Features

#### Main

- **Home Page:** A responsive front page with a clear and simple display of basic information.
- **Featured Stories:** One list each of stories, videos and audio which displays the five most recently uploaded objects for each model.
- **Navbar:** A Bootstrap element used to provide simple navigation to each of the key pages on the site.
- **Search Function:** A global search function which returns results across stories, videos, audio and users.
- **Search Results:** A list page which separates out the results into different tabs for videos, stories, audio and users - this page uses jQuery to show/hide the tabs and change the styles of the buttons used to access the tabs. Currently limited to only show 5 results of each as the pagination became complex for search results and was throwing a number of errors during testing.
User Functions: An easily-accessible menu of options for existing users to login/logout and new users to register.
- **Profile Link:** New users are able to access their profile from every page on the site.
- **Footer:** An extra area for information around copyright and social links.

#### Accounts

- **User Registration:** A registration function using a customised version of Django’s built-in user registration and authentication views - the user inputs a username, email address, password and password confirmation and if the form is valid they are redirected to a page asking them to check their emails for an activation link.
- **MythMaker Model:** I built an extended version of the built-in Django User model to capture some additional fields including a tagline and bio, as well as some images that can be viewed on the User’s profile page.
- **Account Activation:** A personalised HTML email template is sent to the new user which includes a link and an activation token so they can activate their account.
- **Password Reset:** A link which allows a user to reset their password by submitting their email address, using Django’s built-in password reset view.
- **User Profile:** Each user is assigned their own profile page with information specific to them included on it. This also collates a list of the stories, videos and audios they have either liked or uploaded with links to allow them to do this if they do not have any objects in the list.
- **Edit Profile:** The user is able to edit the key information on their profile, including the header and profile images, tagline and bio fields. Specifications for the image files are given as the site layout is dependent on specific image sizes being included on the pages.
- **User List:** Displays all User objects currently hosted on the site, paginated to show 6 results per page in ascending order of ‘date joined’ to show the oldest members at the top.
- **Public Profile:** A separate view of the profile is available to all users which omits certain information and does not allow editing.
- **Benefits Page:** A link is included on the profile page which displays to the user a list of benefits to upgrading to a paid account, including the ability to upload video and audio stories. This also includes a randomised display of one story, one video and one audio as examples of the different story types.
- **Upgrade:** Users are able to upgrade their account by entering their debit card information into a form field provided by Stripe payments.
- **Upgrade Errors:** A custom error page was created to provide next steps for any users who receive a card error when trying to input their card details.
- **Upgrade Success Page:** A custom page displays to inform the user that their upgrade was successful.
- **Cancel Subscription:** A simple two-click option is available for users to cancel their paid subscription. There is a bug in this process which is outlined in the Future Development section.
- **Actions for Premium Users:** Premium members are able to perform a number of functions that are unavailable to free members. Across the site, if-else statements are used to display different options depending on the member type that is currently viewing them - for example, where a Premium member sees an option to upload a video/audio, a free member will see an option to upgrade their membership to Premium if they wish to upload video/audio.

#### Stories

- **Story List:** Displays all Story objects currently hosted on the site, paginated to show 5 results per page in descending date order to show the most recent at the top.
- **Story Page:** Displays the content of the Story as well as some contextual information including the user who wrote the story and the date it was posted. Also includes a ‘Like’ function and a comments section, detailed in the Community section. The sidebar includes a list of other stories uploaded by the same user, in descending order of popularity based on Likes.
- **Upload Story:** Uses a form through which the user can upload a new story, including specifications for the cover image and thumbnail as the site layout is dependent on the images being a certain size.
- **Delete Story:** A button on the story page triggers a modal which asks the user to confirm deletion of the story, if this is confirmed the story is deleted from the database. The ‘delete’ button is hidden from all users except the one who uploaded the story originally, and the view includes a failsafe to ensure that the user requesting the deletion and the user who uploaded the story are the same, otherwise an error is thrown.

#### Videos

- **Video List:** Displays all Video objects currently hosted on the site, paginated to show 5 results per page in descending date order to show the most recent at the top.
- **Video Page:** Displays the content of the Video as well as some contextual information including the user who uploaded the video and the date it was uploaded. Also includes a ‘Like’ function and a comments section, detailed in the Community section. The sidebar includes a list of other videos uploaded by the same user, in descending order of popularity based on Likes.
- **Upload Video:** Uses a form through which the user can upload a new video if they are a Premium member, including specifications for the thumbnail as the site layout is dependent on the images being a certain size.
- **Delete Video:** A button on the video page triggers a modal which asks the user to confirm deletion of the video, if this is confirmed the video is deleted from the database. The ‘delete’ button is hidden from all users except the one who uploaded the video originally, and the view includes a failsafe to ensure that the user requesting the deletion and the user who uploaded the video are the same, otherwise an error is thrown.

#### Audio

- **Audio List:** Displays all Audio objects currently hosted on the site, paginated to show 5 results per page in descending date order to show the most recent at the top.
- **Audio Page:** Displays the content of the audio as well as some contextual information including the user who uploaded the audio and the date it was uploaded. Also includes a ‘Like’ function and a comments section, detailed in the Community section. The sidebar includes a list of other audios uploaded by the same user, in descending order of popularity based on Likes.
- **Upload Audio:** Uses a form through which the user can upload a new audio if they are a Premium member, including specifications for the cover image and thumbnail as the site layout is dependent on the images being a certain size.
- **Delete Audio:** A button on the audio page triggers a modal which asks the user to confirm deletion of the audio, if this is confirmed the audio is deleted from the database. The ‘delete’ button is hidden from all users except the one who uploaded the audio originally, and the view includes a failsafe to ensure that the user requesting the deletion and the user who uploaded the audio are the same, otherwise an error is thrown.

#### Community

- **Like Story:** Gives the user the option to Like a story. This is stored as a ‘Like’ object with a story type of ‘STORY’, and each new like increments the number stored in the ‘likes’ field on the Story object. A user is limited to liking each story once, and a message is flashed if they try and like the same story a second time.
- **Like Video:** Gives the user the option to Like a video. This is stored as a ‘Like’ object with a story type of ‘VIDEO’, and each new like increments the number stored in the ‘likes’ field on the Video object. A user is limited to liking each video once, and a message is flashed if they try and like the same video a second time.
- **Like Audio:** Gives the user the option to Like an audio. This is stored as a ‘Like’ object with a story type of ‘AUDIO’, and each new like increments the number stored in the ‘likes’ field on the Audio object. A user is limited to liking each audio once, and a message is flashed if they try and like the same audio a second time.
- **Comments:** A user can also leave a comment on each of the story types, unlike the Like function this is built into the individual views for the story, video and audio pages. This saves the username, the date the comment was left and the body of the comment and adds to the comments section and total comments count each time a new comment is submitted.

### Future Development

#### Future - Main

- **User Filtering:** I intend to add filters for the user list page to allow users to browse only for Premium members, for example.
- **Search Result Pagination:** Due to the complexities in paginating the different tabs included on the search results page and after some testing and error handling I elected to limit the number of search results in each category to 5 so they would all fit on the same page. For a small number of total objects this works fine but it will need to be changed if the scope of the site was to scale up.
- **Uploaded Image Scale:** I would like to develop the layout of the site to ensure that the image fields are a fixed size and any images a user uploads cannot negatively affect the formatting of the site. Currently I have included helper text on all image upload fields to provide guidance, but I would be keen to try and mitigate the risk of this occurring.

#### Future - Accounts

- **Upgrade Confirmation Email:** I wanted to include an email to users when they have successfully upgraded their account to a premium subscription.
- **Cancellation Bug Fix:** There is a bug in the subscription cancellation process wherein if the user cancels their subscription and then goes through the upgrade process again, the site does not register that they are a paid member once again.
- **Delete Account:** I did not include an option for a user to delete their account at this stage, but feel it would be helpful in future development.

#### Future - Stories

- **Additional Categorisation:** In future I would like to add extra fields to the Story model to capture elements such as genre and word count which would allow for more filtering.
- **Filtering:** With additional categorisation, filters could be applied to the Story List view.
- **Upload Preview:** I would have liked to include a step in which users could preview their story before submitting it to the site.
- **Edit Stories:** There is currently no function to edit stories once they have been uploaded.
- **Archive Story:** Rather than deleting the story outright I would have liked to include a function to archive it for potential future recovery.

#### Future - Videos

- **Upload Preview:** I would have liked to include a step in which users could preview their video before submitting it to the site.
- **Edit Videos:** There is currently no function to edit videos once they have been uploaded.
- **Archive Video:** Rather than deleting the video outright I would have liked to include a function to archive it for potential future recovery.

#### Future - Audio

- **Upload Preview:** I would have liked to include a step in which users could preview their audio before submitting it to the site.
- **Edit Audio:** There is currently no function to edit audio once it has been uploaded.
- **Archive Audio:** Rather than deleting the audio outright I would have liked to include a function to archive it for potential future recovery.

#### Future - Community

- **Un-Like:** Users do not currently have the ability to delete their submitted Likes on stories, videos and audio.
- **Delete Comments:** Users do not currently have the ability to delete their own comments.
- **User-to-User Messaging:** I would have liked the opportunity to include a system for users to send messages to each other outside of the comments sections.

## Testing

I created a suite of automated tests using Django’s built-in testing framework to ensure that the views, forms and models in each app were functioning correctly. I experienced some difficulties with this process as the use of an extended user auth model in the accounts app made creating the test user each time the test database was created a much more complex process.

As such, many of my tests were written after the code itself was completed so the project does not follow a true test-first development practice, however manual tests were completed for each stage of development in an effort to supplement the automated tests. A list of manual test scripts can be found in the testing folder.

Stripe was also extensively manually tested to ensure that relevant errors were thrown when an invalid card number was entered. As a result of this testing a generic error page was included to provide further information on next steps whenever a card error was encountered.

I also used Travis CI to test and ensure continuous integration of my code. This took a number of attempts to set up correctly, which resulted in a high number of Git commits in my repository at the beginning of the development process. The Travis build also began failing part way through the development of the website due to some configuration issues with my PostgreSQL database, however with some assistance from Code Institute Tutor Support I was able to fix this and get the build to succeed before deployment.

I also used the W3 Validation Services for both HTML and CSS, JSLint to validate my jQuery, as well as the built-in Pylint in Visual Studio Code to ensure my code was valid and the syntax was correct.

## Deployment

I deployed the app by.

## Credits

### Content

There was some content.

### Media

The written content of the test objects in the Stories app was taken from public domain literature hosted on [Gutenberg.org](https://www.gutenberg.org).

Test objects in the Video app were found on [Pexels.com](https://www.pexels.com/), a free stock photo and video archive.

Test content in the Audio app was sourced from [LibriVox.org](https://librivox.org), a catalogue of public domain audiobooks and recordings.

### Acknowledgements
# Deployment

## Deploy the Django website on Render

The repository contains a Django website and a separate Streamlit medicine recommender. The Render Blueprint at the repository root creates both web services and a PostgreSQL database.

1. Push these changes to the GitHub repository.
2. In Render, choose **New +** then **Blueprint** and connect `RajuManur143/JanaAushadi_kendra_for_better_health`.
3. Select the `main` branch and apply the Blueprint. Render builds and deploys the service; the generated `onrender.com` address is shown in the dashboard.
4. After the first deploy, open the service's Shell and run `python manage.py createsuperuser` to add the first admin user.
5. Sign in at `/admin/` and add or update records. A migration seeds the six featured Maharashtra stores shown on the site; the repository has no broader official store dataset or medicine catalog fixture.

The settings read `SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS`, and `DATABASE_URL` from the environment. Render generates the production secret and supplies the database URL and host. Do not reuse the Django secret that was committed in the old settings file; it should be treated as exposed.

The contact form also needs `DJANGO_EMAIL_TESTING_ACCOUNT_NAME` and `DJANGO_EMAIL_TESTING_ACCOUNT_PASSWORD` set in Render to send mail through Gmail.

## About Vercel and the recommender

There is no separate JavaScript frontend in this repository: the browser pages are Django templates, coupled to Django routes and forms. Deploying only those templates to Vercel would break those interactions. The working deployment for the existing app is therefore the complete Django site on Render. A Vercel frontend would require a separate frontend project and API integration.

The recommender build step generates compact top-five medicine matches from `recommend/medicine.csv` instead of storing the original dense similarity matrix, which would exceed a free instance's memory.
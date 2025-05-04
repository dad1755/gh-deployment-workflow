# gh-deployment-workflow
GitHub Pages Deployment | Simple GitHub Actions workflow to deploy a static website to GitHub Pages.
GitHub Pages Deployment Workflow

This repository demonstrates a GitHub Actions workflow that automatically deploys changes to index.html to GitHub Pages.

Project Structure





index.html: A simple landing page



.github/workflows/deploy.yml: GitHub Actions workflow configuration



README.md: This file

How It Works





The workflow triggers on any push to the main branch where index.html is modified



The workflow:





Checks out the code



Sets up GitHub Pages



Uploads the repository contents as an artifact



Deploys to GitHub Pages

Setup Instructions





Create a new repository named gh-deployment-workflow



Add the files from this repository



Enable GitHub Pages in your repository settings:





Go to Settings > Pages



Select GitHub Actions as the source



Push changes to the main branch



The workflow will automatically deploy to https://<username>.github.io/gh-deployment-workflow/

Making Changes





Modify index.html to update the website content



Commit and push changes to the main branch



The workflow will automatically deploy the updated page

Requirements





GitHub account



Repository with GitHub Pages enabled



Write permissions for GitHub Pages

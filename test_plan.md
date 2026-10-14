# Test Plan – Job Application Workflow

## Objective
Verify that candidates can locate the right role, understand key details and submit a local application safely. The mock app is used for submission scenarios; no fake applications are sent to a live employer portal.

## Scope
- Listing content: title, salary, experience, description.
- Navigation and invalid role URLs.
- Required fields, malformed email, whitespace and boundary inputs.
- Confirmation, duplicate submissions and repeated-request behavior.
- Slow/failing requests, responsive layout, keyboard use and browser compatibility.

## Priorities
- **P0:** invalid/duplicate submissions and application data integrity.
- **P1:** listing accuracy, navigation, validation, confirmation and failure recovery.
- **P2:** responsive layout, accessibility smoke checks and broader browser coverage.

## Method
1. Confirm environment and test data.
2. Explore listing and detail links.
3. Exercise positive, negative and boundary form scenarios.
4. Automate stable high-priority checks with Playwright.
5. Report only reproduced defects, including environment, steps, expected/actual result and evidence.
6. Rerun and record observed results.

## Entry / exit
Entry: app starts and dependencies are installed. Exit: P0/P1 cases are executed or marked blocked; findings have reproducible evidence; results are documented honestly.

## Browser coverage
The default suite targets Chromium. Install and test Firefox/WebKit separately before claiming cross-browser coverage. Mobile layout and keyboard checks are manual in this starter project.\n
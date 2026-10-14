# Manual Test Cases

Environment: local mock at `http://127.0.0.1:5000`. Record actual result, date, browser/version and evidence after execution. P0 = critical, P1 = high, P2 = medium.

| ID | Priority | Steps / scenario | Expected result | Type |
|---|---|---|---|---|
| TC-01 | P1 | Open jobs landing page. | Role title, salary, experience and description are visible. | Positive |
| TC-02 | P1 | Click View role for QA Engineer. | Correct detail page and URL open. | Positive |
| TC-03 | P1 | Open a nonexistent role URL. | Clear not-found response; no apply form. | Negative |
| TC-04 | P0 | Submit form with both fields empty. | Required validation blocks submission. | Negative |
| TC-05 | P0 | Enter name and malformed email. | Invalid email is rejected; no record created. | Negative |
| TC-06 | P1 | Enter whitespace-only name and valid email. | Name is rejected after trimming. | Boundary |
| TC-07 | P0 | Submit valid name and email. | One confirmation appears. | Positive |
| TC-08 | P0 | Submit same email for same role twice. | Second submission is rejected as duplicate. | Negative |
| TC-09 | P1 | Submit same email for another role. | Behavior matches documented duplicate policy; mock key is role + email. | Boundary |
| TC-10 | P1 | Use `qa+test@example.com`. | Plus-address email is accepted. | Boundary |
| TC-11 | P1 | Enter a 200-character name. | No crash/layout break; max length is documented if applicable. | Boundary |
| TC-12 | P1 | Refresh after successful submission. | No silent duplicate POST; browser behavior is safe. | Negative |
| TC-13 | P1 | Use Back from detail to listing. | Listing returns and links remain functional. | Navigation |
| TC-14 | P2 | Resize to 375 px width. | No horizontal overflow; form remains readable. | Compatibility |
| TC-15 | P1 | Simulate slow response in a controlled local environment. | Feedback is clear and repeated requests are prevented. | Resilience |
| TC-16 | P1 | Simulate server/network failure locally. | Clear error and recoverable form state. | Resilience |
| TC-17 | P2 | Run smoke checks in Chromium, Firefox and WebKit. | No browser-specific blocker; differences documented. | Cross-browser |
| TC-18 | P1 | Add leading/trailing spaces to inputs. | Inputs are normalized safely. | Boundary |
| TC-19 | P2 | Navigate using keyboard only. | Logical focus order and accessible labels. | Accessibility |
| TC-20 | P1 | Compare listing details with approved source. | Salary and experience match source exactly. | Data integrity |

## Execution record
Do not prefill pass/fail. Record date/time, browser/version, actual result, notes and evidence path for every executed case.\n
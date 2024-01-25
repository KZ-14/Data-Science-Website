# MARICO-DATA-SCIENCE
## Overview

The primary objective of hosting a data science website is to centralize and streamline the access to various departmental dashboards, ensuring a balance between security, user satisfaction, and decision-making support for higher management. 

## Key Points

- Nginx serves as the web server and proxies requests to Django.
- Django handles authentication and authorization using Azure AD.
- Azure AD validates user credentials and grants access if authorized.
- Access tokens are used to secure communication between Azure AD and Django.
- Users are only granted access to specific dashboards based on their authorization.
- Unauthorized users are denied access and receive an appropriate message.


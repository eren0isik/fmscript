# DATABASE

- We customized and used FMDB as our database.
- FMDB is our own database system.
- All data is encrypted, and it is very difficult to decrypt it without a key file.
- If there is no query opening, your data cannot be stolen in any way.
- You can carefully pull the key from another server to enhance security. Thus, if the system is breached, your database cannot be opened outside of that server.
- You can customize the model by editing the model function in `extensions.py`.

# FRAMEWORK

- We used Flask.

# CUSTOMIZATION

- We used the blueprint system, allowing you to customize the content as you wish.
- After adding your page file into the Blueprints folder, you can verify it in the `__init__.py` file under the `app` folder. An example of this verification process is included within the `__init__.py` file.
- There is no limit to customization.
- There is an example of a login system included. Since we built it with the FMDB infrastructure, we used FMDB; however, you can choose other alternatives if you wish.

# FRONTEND

- The frontend part is entirely Flask. If you are familiar with Flask, you can skip this part.
- You can use anything you want, such as HTML, CSS, and JS.
- Frontend files are stored in the `templates` directory. You can modify this by adding a small piece of code to the backend if desired.
- CSS and JS files are stored in the `static` directory.
- You can understand the working principle by examining the examples.

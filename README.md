# Hexrail
Hexrail is a emulated CLI-based OS. It is NOT completely open-source: Hexrail apps are closed-source. The apps are source available, but we DON'T allow to users edit Hexrail apps and publish it.

# Required modules and apps to run Hexrail
Termcolor, install it via: ```pip install termcolor```. (Install Python3 first)
Python, install it via: ```sudo apt install python3```. (for Linux, Debian machines)

# Making an app for Hexrail
Its very easy. First of all, you need a basic Python programming knowledge.
Make sure that Python3 and zip is installed on your Linux machine.

# Step 1: Making app

Go to the main hexrail folder.

```
mkdir myapp
```

This command creates a folder called "myapp".

# Step 2: Making app

Now, we need to program this folder using Python.

```
cd myapp
nano main.py
```
Now, program this folder. I'm gonna program this as print("Hello, World!") code. Press CTRL + O to save it, CTRL + X to exit.

# Step 3: Making app

Now, we are gonna HPKG this using zip.

```
zip -r -X ../myapp.hpkg *
```

# Step 4: Making app

```
cd ..
```

# Step 5: Making app

```
mv myapp.hpkg repo/
```

Now we builded our first app. To test it, we are going to use package manager. Go to the step 6!

# Step 6: Making app

```
python3 package_manager.py
```
Warning: Never use python command, instead use python3 command.

# Step 7: Making app

We are gonna install the package.

```
install myapp.hpkg
```

# Step 8: Making app (FINAL STEP)

Now we are ready to run our first app.

```
run myapp
```

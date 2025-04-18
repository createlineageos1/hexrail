# Hexrail
hexrail is a emulated CLI-based OS, and based on the OrbitOS kernel

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

# Hexroid
Hexroid is a emulated CLI-based OS. It is NOT completely open-source: Hexrail apps are closed-source. The apps are source available, but we DON'T allow to users edit Hexrail apps and publish it.
Hexrail is replaced by Hexroid, but its based on Hexrail system.

# Required modules and apps to run Hexroid
Termcolor, install it via: ```pip install termcolor```. (Install Python3 first)
Python, install it via: ```sudo apt install python3```. (For Linux, Debian machines)
(If you want to ask math questions to Hexroid Zeus and u have CUDA GPU:) PyTorch GPU, install it via ```pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118```. (For CUDA GPUs, for Hexroid Zeus and Victus 1M)
(If you want to ask math questions to Hexroid Zeus and u have CPU:) PyTorch CPU, install it via ```pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu```. (For CPUs, for Hexroid Zeus and Victus 1M)

# Testing
We are testing Hexroid/Hexrail versions in our home datacenters/servers.

# Making an app for Hexroid
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

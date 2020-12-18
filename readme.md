# Professor-Pages

This Python Package is a command line tool for creating HTML pages concerning University Professor web-pages.

### Installation 

<!-- todo -->

### Basic Usage

<!-- todo -->

### Overall Code Description

1. `ui` handles User commands.
It translates command line input into Controller calls.

2. `ctrl` is a layer between User Interface, Repository and HTML output.
It translates UI commands into In-Memory data.
It also translates In-Memory data into actual HTML Pages.

3. `repo` handles In-Memory data.
It does basic CRUD operations on the Domain classes

    - Create data
    - Read data
    - Update data
    - Delete data

On every program run, the `repo` will read the data from some .csv formatted files
and overwrite them when changes are made.

4.

    a. `domain.data` handles basic data classes. 
These classes will be used by the Repository to store data.

    b. `domain.view` handles python to HTML translation classes / functions.
They will be used by the Controller to create HTML Pages.


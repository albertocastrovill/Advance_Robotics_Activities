# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.22

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/albertocastro/Documents/UDEM/RoboticaAvanzada/Advance_Robotics_Activities/C++_Codes

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/albertocastro/Documents/UDEM/RoboticaAvanzada/Advance_Robotics_Activities/C++_Codes/build

# Include any dependencies generated for this target.
include CMakeFiles/productTwo.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include CMakeFiles/productTwo.dir/compiler_depend.make

# Include the progress variables for this target.
include CMakeFiles/productTwo.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/productTwo.dir/flags.make

CMakeFiles/productTwo.dir/main.cpp.o: CMakeFiles/productTwo.dir/flags.make
CMakeFiles/productTwo.dir/main.cpp.o: ../main.cpp
CMakeFiles/productTwo.dir/main.cpp.o: CMakeFiles/productTwo.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/albertocastro/Documents/UDEM/RoboticaAvanzada/Advance_Robotics_Activities/C++_Codes/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/productTwo.dir/main.cpp.o"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT CMakeFiles/productTwo.dir/main.cpp.o -MF CMakeFiles/productTwo.dir/main.cpp.o.d -o CMakeFiles/productTwo.dir/main.cpp.o -c /home/albertocastro/Documents/UDEM/RoboticaAvanzada/Advance_Robotics_Activities/C++_Codes/main.cpp

CMakeFiles/productTwo.dir/main.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/productTwo.dir/main.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/albertocastro/Documents/UDEM/RoboticaAvanzada/Advance_Robotics_Activities/C++_Codes/main.cpp > CMakeFiles/productTwo.dir/main.cpp.i

CMakeFiles/productTwo.dir/main.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/productTwo.dir/main.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/albertocastro/Documents/UDEM/RoboticaAvanzada/Advance_Robotics_Activities/C++_Codes/main.cpp -o CMakeFiles/productTwo.dir/main.cpp.s

CMakeFiles/productTwo.dir/product.cpp.o: CMakeFiles/productTwo.dir/flags.make
CMakeFiles/productTwo.dir/product.cpp.o: ../product.cpp
CMakeFiles/productTwo.dir/product.cpp.o: CMakeFiles/productTwo.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/albertocastro/Documents/UDEM/RoboticaAvanzada/Advance_Robotics_Activities/C++_Codes/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object CMakeFiles/productTwo.dir/product.cpp.o"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT CMakeFiles/productTwo.dir/product.cpp.o -MF CMakeFiles/productTwo.dir/product.cpp.o.d -o CMakeFiles/productTwo.dir/product.cpp.o -c /home/albertocastro/Documents/UDEM/RoboticaAvanzada/Advance_Robotics_Activities/C++_Codes/product.cpp

CMakeFiles/productTwo.dir/product.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/productTwo.dir/product.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/albertocastro/Documents/UDEM/RoboticaAvanzada/Advance_Robotics_Activities/C++_Codes/product.cpp > CMakeFiles/productTwo.dir/product.cpp.i

CMakeFiles/productTwo.dir/product.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/productTwo.dir/product.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/albertocastro/Documents/UDEM/RoboticaAvanzada/Advance_Robotics_Activities/C++_Codes/product.cpp -o CMakeFiles/productTwo.dir/product.cpp.s

# Object files for target productTwo
productTwo_OBJECTS = \
"CMakeFiles/productTwo.dir/main.cpp.o" \
"CMakeFiles/productTwo.dir/product.cpp.o"

# External object files for target productTwo
productTwo_EXTERNAL_OBJECTS =

productTwo: CMakeFiles/productTwo.dir/main.cpp.o
productTwo: CMakeFiles/productTwo.dir/product.cpp.o
productTwo: CMakeFiles/productTwo.dir/build.make
productTwo: CMakeFiles/productTwo.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/albertocastro/Documents/UDEM/RoboticaAvanzada/Advance_Robotics_Activities/C++_Codes/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Linking CXX executable productTwo"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/productTwo.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/productTwo.dir/build: productTwo
.PHONY : CMakeFiles/productTwo.dir/build

CMakeFiles/productTwo.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/productTwo.dir/cmake_clean.cmake
.PHONY : CMakeFiles/productTwo.dir/clean

CMakeFiles/productTwo.dir/depend:
	cd /home/albertocastro/Documents/UDEM/RoboticaAvanzada/Advance_Robotics_Activities/C++_Codes/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/albertocastro/Documents/UDEM/RoboticaAvanzada/Advance_Robotics_Activities/C++_Codes /home/albertocastro/Documents/UDEM/RoboticaAvanzada/Advance_Robotics_Activities/C++_Codes /home/albertocastro/Documents/UDEM/RoboticaAvanzada/Advance_Robotics_Activities/C++_Codes/build /home/albertocastro/Documents/UDEM/RoboticaAvanzada/Advance_Robotics_Activities/C++_Codes/build /home/albertocastro/Documents/UDEM/RoboticaAvanzada/Advance_Robotics_Activities/C++_Codes/build/CMakeFiles/productTwo.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/productTwo.dir/depend


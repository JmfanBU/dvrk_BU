file(REMOVE_RECURSE
  "dvrk_teleop_gui_automoc.cpp"
)

# Per-language clean rules from dependency scanning.
foreach(lang )
  include(CMakeFiles/actionlib_generate_messages_py.dir/cmake_clean_${lang}.cmake OPTIONAL)
endforeach()

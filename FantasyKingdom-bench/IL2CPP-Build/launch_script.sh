#!/bin/bash

bash measureECMacos.sh "open -W IL2CPP-Dev-FasterBuild-Release-Build.app" 30 IL2CPP-Dev-FasterBuild-Release-Build
bash measureECMacos.sh "open -W IL2CPP-FasterBuild-Release-Build.app" 30 IL2CPP-FasterBuild-Release-Build
bash measureECMacos.sh "open -W IL2CPP-Dev-FasterRuntime-Release-Build.app" 30 IL2CPP-Dev-FasterRuntime-Release-Build
bash measureECMacos.sh "open -W IL2CPP-FasterRuntime-Release-Build.app" 30 IL2CPP-FasterRuntime-Release-Build
bash measureECMacos.sh "open -W IL2CPP-FasterBuild-Master-Build.app" 30 IL2CPP-FasterBuild-Master-Build


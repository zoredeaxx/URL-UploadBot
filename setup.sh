run_command: cd && mkdir -p bin/ffmpeg-build && pushd bin/ffmpeg-build && wget https://johnvansickle.com/ffmpeg/builds/ffmpeg-git-amd64-static.tar.xz
    && tar xf ffmpeg-git-amd64-static.tar.xz && cd ffmpeg-git-20220910-amd64-static
    && mv * ../../ && popd && rm -rf ./bin/ffmpeg-build && export PATH=$PATH:/workspace/bin
    && python3 bot.py

@echo off
for %%f in (*.md) do (
  echo Converting %%f...
  pandoc "%%f" -t revealjs -s --slide-level=3 ^
    -V revealjs-url=https://unpkg.com/reveal.js@5 ^
    -V theme=white -V slideNumber=true ^
     -V center=false ^
    -o "%%~nf.slides.html"
)
echo Done!
pause

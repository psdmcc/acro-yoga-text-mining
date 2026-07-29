
# Step 5: Trigger LuaLaTeX document build sequence to output updated PDF
if [ -f "main_article_new.tex" ]; then
    echo -e "$INFO Generating updated academic manuscript PDF via LuaLaTeX..."
    lualatex --interaction=nonstopmode main_article_new.tex > /dev/null
    bibtex main_article_new > /dev/null
    lualatex --interaction=nonstopmode main_article_new.tex > /dev/null
    echo -e "$SUCCESS Document compiled successfully."
else
    echo -e "$ERROR main_article_new.tex not found in root workspace directory. Skipping typeset node."
fi

# Spielman group papers

[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)

This is a template for starting papers in the Spielman group that has standardized places for all the files to go.  The idea is to clone this into your project's new repo and then link to overleaf or edit on your local machine.  You should consider the workflow of writing a paper no differently from software and take advantage of revision control.  This implies that we should not maintain old versions documents, figures, or whatever.  Instead to get those, we just revert to a past version of the repository on our local machines.

Notice that the figure files go in the root directory.  This is because Physical Review journals currently do not allow directories in their submission (but arxiv does), so conforming to this standard here will make submission easier.

# Starting the writing process

Generally you should begin writing by making a schematic representation of your manuscript (this might be an outline, or a sketch of figures, it really depends on your internal representation of your result).  Starting from this schematic you need to identify the following:

1. **Base Context:**  Make a list (really\!) of the base knowledge you assume every reader has.  Some readers will have additional specialized knowledge, so you might make a second list of different places different readers might be coming from.  
1. **Results:** What have you measured or computed or discovered that forms the core essence of your manuscript  
   1. *Base Argument:* What is the experimental and/or theoretical argument leading to this result?  
2. **Paper structure:** Given your understanding of the base context of your readership and the argument leading to your results, you need to produce a self-contained manuscript that *does not* assume any knowledge that lies outside of the base knowledge you have assumed.  Divide the paper into organizational sections that:  
   1. *Place the work in context:* tell you readers where this work fits into the overall scientific framework, and why they should be interested.  
   2. *Set the stage*: inform the readers of the things they need to know to get your result.  This often includes introducing concepts that lie outside of the base knowledge that you earlier defined.  
   3. *Present the argument*: just like it sounds, now you lead the readers through the experimental and theoretical maze leading to your final results.  
   4. *Wrap it up*: in a long document you might summarize your argument, but in any case, this is your opportunity to present some outlook that only becomes relevant to the readers once they can look back on your arguments.  Otherwise you would have placed this in the introduction.

# Figures

Everybody will have their own style for making figures, but for a quality result there are some common points that I’ll describe here.  **Above everything else, a figure should *clearly* communicate to the reader its intended content.**  To do so consider the following advice, but remember that every “rule” has exceptions, and that clarity is the goal:

1. **Quality**.  If the figures look shoddy, I will presume the science is also shoddy, making an uphill battle to demonstrate otherwise.  That is to say, that attention to detail in the manuscript suggests a similar attention to detail in the science.  
2. **Consistency**.  In a given manuscript, the figures should have a common appearance, and should be well matched with the surrounding text.  This implies:  
   1. *Fonts*. the fonts should be selected to match the manuscript font in style and size.  Generally the caption will have 8 to 9 point fonts, and your figures should match this, with larger font (say 9 to 10 pts) for large labels, medium (say 8 or 9 pts) for axes labels, and small (8 or below) for annotations / insets.  
      1. For Phys. Rev. journals I use LaTeX fonts in the figures, and I find the Stix fontset ([www.**stixfonts**.org](http://www.stixfonts.org)) is pretty good for graphics programs like Illustrator (or shudder… Inkscape).  
      2. I use LatexIt on the mac to generate equations, or with matplotlib in python, I get this for free.  
   2. *Line widths*.  Typically you want 0.75 or 1 pt lines for the axes, and for most curves, but this can vary for emphasis.  
   3. *Symbol size*.  Generally make the symbols modest sized (about the size of a “o” in the legend font), unless there are 100’s of symbols in which case you should consider using points.  
   4. *Colors*.  Be consistent from figure to figure.  Keep in mind people can be color blind.  
   5. *Margins*. Pick standard margins and use them.  Side-by-side figures should be the same height and vertically stacked figures should have the same width.    
3. **Clarity over clutter.**  Each figure is there for a reason (right?), so be sure that it conveys the intended information, and is not cluttered with graphical excess that is not part of the message.  **Every single graphical element of a figure is placed there by you with a specific intention to convey information or as part of a specific aesthetic goal.**  With that in mind:  
   1. *Default*: your default figure is a black-and-white line drawing.  Added elements can and should be there, but with intent.  
   2. *Avoid*:  
      1. 3D drawings unless you are really conveying 3D information.  
      2. Glitz effects such as shadows, reflections.  
   3. *Use*:  
      1. Line styles (dashed, dotted, bold), colors, symbols, equations, **but only when needed.**  
      2. Shared axes: if two side-by-side or stacked graphs share the same vertical (side-by-side) or horizontal (stacked) axes, then omit all labels on the “inner” axes.  
   4. *Do:*  
      1. Make lines line up between different plots in the same figure.  
      2. Unless it is pathological (like data with a range from 0.9999 to 1.0), make axes start at zero.  
4. **Figure captions:** In general the figure caption should give the information required to understand the content of the figure such as “Dispersion relation. Black symbols denote the measurements of momentum and the red curve is our model fit to the data.”  The caption should *not* describe the scientific payload of the figure or interpret the content of the figure.  This belongs in the text.  
   1. There are exceptions to this.  For example, in lay-public magazines such as Scientific American the figures together with the captions should “tell the story” even in isolation from the body of the text.  
5. **Pet peeves**: This is just style, but I will mark it up on papers.  
   1. Don’t connect data points with lines *unless you believe that the lines extrapolate to, where in the intervening space, a data point would lie.* What this means is that if you have significant scatter in your data, you should not be connecting those points with a jagged line.  If you want a guide to the eye just fit to some random function that passes through the data within the uncertainty and say it is a guide to the eye in the caption.

   
One specific tip for helping with this is to prepare the figure exactly the same size it will appear in the manuscript.  For example in Phys. Rev. journals the column width is 3.375 in, so make the figure 3.375 in wide in your preparation software (this becomes 7.0 in for a two column width figure) and latex code like

```
\begin{figure}
\begin{center}
\includegraphics{Fig1_Awesome_Figure.pdf}
\end{center}
\caption{
(Color online) (a) This is without doubt the most awesome figure ever.
}
\label{fig:awesome}
\end{figure}
```

to deploy the figure.  This will make sure that all of your work selecting font sizes translates to the final product.  This means avoid `\includegraphics[width=0.43\columnwidth]` or `\includegraphics[width=3.3in]` like the plague as they will alter your figures in a generally unpredictable way, often leading to ghastly results.

# Prose

Like figure preparation, prose differs greatly from individual to individual, but good clear writing has some rules of thumb (that can be broken, never fear).  **The prose of your manuscript serves to _clearly_ convey your scientific findings and your *excitement* in these findings to the soon to be enthralled reader.**  The following are some general points which I critique all the time.

1. **Don’t assume, instead explain.**  You have been working on this project for months/years and everybody around you knows all about it.  Trust me: the rest of the world does not.  Make your argument clearly and with style.  
2. **Be concise.**  Only use low content phrases with specific intent to highlight something: avoid needless words.  Examples of these phrases include  
   1. “It follows that, ...”  
      1. Generally just drop this text  
   2. “Evidently...”, “Clearly…”, “Trivially…”, “In fact…”, “note that…” and so forth.  
      1. Just drop these phrases.  
   3. “In the following” or “In what follows”  
      1. Usually omitted, but sometimes useful.  
   4. “Here,” Where else would it be exactly? in some other paper?  
      1. Usually omitted, but occasional use is good for focus.  
   5. “Have”, “has”: usually this can be dropped.  
3. **Be consistent**.    
   1. *Tense*. I don’t know what is right, but *do* use tense consistently in any given paper.  For example, I typically suggest expressing the experiment and data taken in the past, and the understanding in the present.   This is my style, but I am not bothered when I read papers which consistently use a different tense convention.  
   2. *Spelling*.  US versus Imperial.  Pick one.  
   3. *Acronyms/abbreviation*: they are needed, but keep them to a minimum, and always define them at their first use.  Also, an abbreviation defined in the abstract must be redefined in the main body of the text.  
4. **Minitua**:  
   1. $^{40}{\rm K}$: notice K is in a Roman font.  
   2. 40 s: notice space between number and unit, and notice the unit is in Roman font.  
   3. Don’t do a stacked fraction such as $\frac{a}{b}$ in an inline equation do $a/b$ instead.  
      1. Point of mixed opinion: how should ab cbe rendered inline?  I used to prefer $a/bc$, but it has been correctly pointed out that this is ambiguous and $a/(bc)$ is more clear, so I now favor the latter.  
   4. $p$\-wave: notice italics on $p$ because it is referring to a symbol.  
   5. Subscript rules:  
      1. $I_{\rm sat}$: sat is in Roman because it is part of a word  
      2. $m_F$: $F$ is in italics because it is a symbol.  
      3. $\mu_{\rm B}$: B is in Roman because it is an abbreviation of Bohr, and it is caps because Bohr is a name.  If it was referring to the magnetic field $B$ then it would be in italics.  
   6. Use the usual rules of capitalization prior to the introduction of an acronym.   
      1.  Consider the example Bose-Einstein condensate (BEC).  Notice that Bose and Einstein are capitalized (because they are proper names) and condensate is not.  
      2. So it is not correct to write “Please Love My Dog (PLMD),” instead just use “please love my dog (PLMD).”  
5. **Pet Peeves**.  Like with the figures, these are my pet peeves, and not really rules.  
   1. Avoid section breaks in a Letter: the document is so short to start withh.  Still, it can be useful to identify sections with "_Discussion -- _` to give some visual break.  
   2. Lines are straight, curves can be curvy or straight.  Do not describe a curve in a figure as a line unless it is straight.  For example, in describing a fit to data, say “In Fig. 7, the black symbols represent the data, and the red curve depicts a polynomial fit to the data.”  
   3. It is common for people to write things akin to “In recent years there has been a growing interest in …” in the introduction to papers.  **Don’t do this**. This just tells me that you are some sort of lemming, and indicates that the following work is unlikely to be interesting.  Focus on the intrinsic interest of *why* there has been “growing interest” and discuss that instead (and provide references to all these papers that evidence the growing interest).

   
Do try to get some friends to proofread your writing, and don’t get too invested in your prose.  You are trying to be clear, so *be receptive* to advice.    

Title: Complete guide to contributing to Academic Publications
Date: 2017-12-27 16:03:45 -0300
Category: Guide to the site
Lang: en
Tags: guide

[![GitHub release](https://img.shields.io/github/release/fhcflx/alt-pub.svg)](https://github.com/fhcflx/alt-pub/releases?colorB=dd4814)
[![Project DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.845747.svg)](https://doi.org/10.5281/zenodo.845747)
[![Article DOI](https://img.shields.io/badge/ARTICLE--DOI-10.6084/m9..5435968-dd4814.svg)](http://dx.doi.org/10.6084/m9.figshare.5435968)
[![pdf](https://img.shields.io/badge/pdf-download-dd4814.svg)]()

This guide will walk you through the steps to contribute in an ethical and free manner to the Academic Publications page, and actively participate in the [Open Science][ca]  movement [1]. Any issues may be addressed to the project's author e-mail ([fhcflx@outlook.com][mail]) or to his Twitter [@fhcflx][twit]. The project is free to be copied, modified and hacked. Comments and contributions are most welcome! Science must be made by all people and freely benefit all people!

## Why Contribute to Academic Publications?

There are more and more ways of publishing all types of academic and non-academic material. Preprints, postprints, self-archiving, conference poster and slides and other resources presented at meetings, congresses, etc. Raw data from research, experimental design, projects for funding agencies or review boards, monographs, reviews, comments, peer reviews. The diversity of materials that can be published in some form in electronic format will only be limited by human imagination. In the future, this promises to be the source of a major revolution in scientific research and will give rise to new fields of study, such as [scientific meta-research][meta] [2], research about the research.

So, why another electronic publishing medium? Besides, this medium has no features that other channels strive to possess, such as peer review, indexing, automatic [DOI][doi] number assignment, and more. The truth is that this project constitutes only one among many. In this way, I do not really see weakness, because the future volume of data produced by humanity will be so great that there will always be room for practically all initiatives. However, I have identified some gaps in the most popular projects these days, in which I would like to innovate, making Academic Publications really the only one of its kind:

1. **This is a community-driven and decentralized project.** Although having a single repository (currently), and having only one administrator (for now), this project can accept an unlimited number of contributions and participants.
2. **This is a completely hackable project.** Just need to have an account on the remote [Git][git] server we use now ([GitHub][github], but it may not be the one used in the future, nor the only one) and contribute. You can change just about everything. The more the community contributions increase, the more the project will change and be shaped in a manner of its own. The power of [Git][git] local versioning management will allow the community to easily use any remote server it wants, even several of them at the same time in the future.
3. **This is a secure project.** Using [GPG keys signatures][gpg], authors can rest assured of protecting their authority and precedence over their work. The project is based on the idea of ​​free access, but with attribution of authorship. Thus, it is completely plagiarism-proof (plagiarism can occur, but with [GPG keys signatures][gpg] it will be possible to immediately prove authorship).
4. **This is a fully citable and traceable project.** Using existing electronic archiving platforms ([figshare][figshare] and [Zenodo][zenodo]), a [DOI][doi] number can be assigned to the project as a whole and to each publication in particular. For example, this text is registered in [figshare][figshare] with [DOI][doi] 10.6084/m9.figshare.5735136 and the complete project (current version of Academic Publications) is registered in [Zenodo][zenodo] with [DOI][doi] 10.5281/zenodo.594582. There are ways to automate this process, but to perform a minimum quality check, the ideal is to keep the process through curatorship.
5. **This is a project with community-verified quality.** Instead of an editor(s) as usual publishing channels, this project will have a curator(s), who will look after the minimum quality standards and organization of the contributed material. Over time, the community will actively critique and review posts by commenting, opening [issues][issue] and making [pull requests][pull].
6. **This is a cool project!** I strongly believe in community participation in science communication projects and integration of scientific knowledge. Creating this project and being part of it, even if it does not get a great resonance, is already a great privilege! It's one of the coolest things I've ever done!

## Contribution formats:

This project is not a scientific journal, has no ISSN number registration, nor is it indexed in any academic database. There are simple ways to index work on Google Scholar, which we describe elsewhere. Thus, it is not correct to refer to the material posted here as having been "published", nor register this information in curricula. While personally advocating a less restrictive view of _publishing_ (hence the title of the project), this distinction is necessary to avoid abuse. It should be made clear that a "publication" (if you want to call it that way) in this project is not a "peer-reviewed publication in an indexed journal". More appropriately, the contribution of unpublished material is to be called as _preprint_ and of previously published material as _postprint_. These are the two basic modalities of _contributing_ supported by this project.

That being said, this is a non-exhaustive list of formats that can be submitted:

1. **Preprint:** academic material written for the purpose of publication in a traditional journal or other publication channel, deposited **before** submission and peer review . More recently, a number of preprints never get published in peer-reviewed channels, retaining their pre-publishing status, and even being quoted as preprints. A precondition for depositing _[preprints][preprint]_ is to check if the vehicle where the final publication is desired allows this practice.
The same formats that can be published in a conventional channel can be deposited as preprints:
  - **articles**
  - **reviews**
  - **commentaries** (letters) and other forms of _front matter_
  - **brief communications**, etc.
2. **Postprint:** less common practice until the emergence of channels such as Researchgate, [figshare][figshare], [Zenodo][zenodo] and others. It is the deposit of material **after** submission, peer review and publication in traditional channels. A prerequisite for this modality is the ownership of authorship rights over the work by the authors. Some traditional journals allow for the deposit in institutional repositories.
As with preprints, the same formats can be deposited as [postprints][postprint].
3. **Self-archiving:** an arbitrary distinction in relation to the modalities described above. It can be said that both the pre and postprints deposited by the author are forms of self-archiving. In this way, it becomes less relevant to distinguish this modality. It could be said, more specifically, that texts created exclusively for self-archiving - or no longer intended for publication (eg material submitted but not accepted in some publication channel) could fall under this definition. However, a less strict definition of _preprint_ also encompasses these assumptions. Institutional depositing of _postprint_ material can also be refered this way.
4. **Research material:** experimental designs, research projects, raw data, statistical analysis, research notebooks, and any other materials, texts, figures, collections of data that may be deposited in a **free and accessible** form, under a license compatible with [Open Science][os] (in most cases, [Creative Commons Attribution 4.0][ccby]). Any posted material will automatically be publicly available. That said, it is a great way to show the community the progress of a research line.
5. **Conference presentation:** posters, slides, abstracts, extended abstracts, complete articles published in conference proceedings. Once again, only material whose authors own the copyright may be posted.
6. **[Grey literature][grey]:** according to the Prague definition, "that which is produced on all levels of government, academics, business and industry in print and electronic formats, but which is not controlled by commercial publishers, i.e., where publishing is not the primary activity of the producing body" [3]. Most of the time, internal publications and alternative formats in public or business institutions. In the less restricted definition of Farace & Schöpfel [3], it includes white papers, blog posts, technical manuals, and many other non-traditional forms of academic material. The authors' copyright control requirement also applies.

## Instructions for Authors:

Only academic material will be accepted. No advertising or commercial material may be included. If the authors intend to use some or all of the material to be contributed in a commercial venture in the future, it is recommended that the contribution not be made. For all formats, authors must submit their full name and affiliation. In addition, they are asked to write three or four lines (around 200 to 400 characters) to show on the main page as a summary of the post.

### Limits for contributed material:

- **Preprint:** There are no limits on number of characters or requirements for posting. All texts will be converted using the program [Pandoc][pandoc] in [Markdown][markdown] format and later parsed into files in `pdf` format. The final aspect is standardized and an example of the typography used can be seen here. Texts in draft format, revision format or final submission format for another publication medium may be accepted. Audio-visual material (figures, graphics, videos, sound) can be received in any format (individual files), but there is no guarantee that they can always be included in the final result, depending on the limitations of the infrastructure used (see next subsection). Authors should first check whether the media to which they wish to submit their papers at a later stage is compatible with preprint (see next section). At this time, it is only possible to receive submissions in Portuguese and English and in the formats supported by the [Pandoc][pandoc] program (see next subsection).
- **Postprint:** The same as for preprints applies here. The difference is that authors should keep full copyright on their works. If you have signed a copyright transfer term to another medium, this is no longer possible. Some journals and publishing media allow for self-archiving of _drafts_ by the author (next section).
- **Self-archiving:** the same limitations of text and audiovisual resources. The authors should state that, at least at the moment, they do not intend to publish the material. However, no obligation is required (authors are free to change their mind in the future and publish their material, in which case _self-archiving_ is a form of _preprint_).
- **Research material:** in addition to text and audiovisual material, it may include spreadsheets and databases. Supported formats are listed in the next subsection. Authors should attach an "abstract" or explanatory text, arbitrarily concise, provided enough to explain what the shared dataset is about. *No information concerning human experimentation will be accepted if any participant may be identified directly or indirectly* (see subsection on _desidentification_).
- **Conference presentation:** The best way to post posters and slides is to deposit them into a specialized service such as [Slideshare][slide] and include them on the post page. If the authors do not want this solution, you can include a link to download the presentation file. Authors should attach an "abstract" or explanatory text, arbitrarily concise, provided enough to explain what the presentation is about. They should also indicate in which event (full name, place and date) the presentation occurred. The contribution of abstracts, extended abstracts and complete articles published in proceedings goes in the same way as the postprint of peer-reviewed material.
- **Grey literature:** In general, the same limits of format, content and ethical restrictions apply to this type of material.

### Formats accepted:

- **Text:** plain text (`.txt`), microsoft office (` .doc, .docx, .rtf`), open office (`.odt, .fodt`), [Markdown][markdown] (many "flavors") , html, LaTeX, reStructuredText.
- **Images:** any format, but only the `jpg, png` and` gif` formats can be viewed on the page. Others can be converted or attached as links to download the files. It is possible that very large images or some formats may not be supported by the [GitHub Pages][githubp] infrastructure where the page is hosted.
- **Graphics:** R and LaTeX codes will be accepted to be converted into images with rmarkdown.
- **Video:** the preferred way to contribute videos is to upload them to [Youtube][youtube] or similar services and then embbed it in the page.
- **Audio:** any format, but files will only be available for download. Size limits may apply.
- **Sheets:** any format, but only the `csv` format can be viewed on the page. Others can be converted or attached as links to download the files.
- **Databases:** any format, but files will only be available for download. Size limits may apply.

## Ethical disclosure:

### Preprint compliance:

Authors who contribute with preprints should check that the vehicle for which the final submission is intended complies with this practice. On the [SHERPA/RoMEO][sherpa] project page one can easily search for the name or ISSN of journals. Vehicles listed as "green" allow pre- and postprint. As a rule of thumb, any work published on Open Access vehicles with a [Creative Commons][cc] license can be auto-archived. If there are any questions, the author of this project can help.

### Ethics for the use of experimental animals:

For the contribution of self-archiving or research materials using experimental animals, the **project acceptance letter** by a **[Committee on Animal Research and Ethics][duly]** must be submitted with the contribution. Postprints, once they have already passed through editorial and peer reviews, are exempt.

### Ethics for human experimentation:

For the contribution of self-archiving or research materials on human experimentation, the **acceptance letter** of the project by an **[Institutional Review Board][dc]**, in addition to the **informed consent form** signed by each participant (or legal representative) must be sent together with the contribution. Postprints, once they have already passed through editorial and peer reviews, are exempt.

Likewise, materials that have not been properly desidentified will not be accepted. This process aims to avoid the direct or indirect identification of the experimental subjects in a clinical study. Typically, simply remove the following items from the results, databases, or text:
- Name, including initials or surnames.
- Provenance, even the city. If necessary to identify patients from more than one treatment center, code the information (eg "center A").
- Date of diagnosis, date of last information collected, date of birth, other dates.
- Other information that, in combination, may identify the research subjects.
Likewise, in the contribution of audiovisual material from clinical studies, those that allow person identification will not be accepted. For example: photos of the whole face can not be accepted, only of parts of the face, discharacterizing the identity.

## Attribution of [DOI][doi]:

In order for the post to have a [DOI][doi] number assigned, you will need to deposit the files in [figshare][figshare], or another compatible service. The authors themselves can do this, or they must clearly state in the contributed material an *authorization* so that the author of this project can deposit it on their behalf.

## Submission of contribution:

### Using Git and GitHub:

- If you already have an account in [GitHub][github] and you already know how to use [Git][git], _fork_ and clone the project, add your [Markdown][markdown] files in the  `content / posts` folder (in Portuguese and/or English), add figures in `content / images`, add pdf in` content / docs` and make a _[pull request][pull]_.
- If you do not know any of this yet but would like to learn, [GitHub][gittut] and [Atlassian][atlassian] have great tutorials!
- Enjoy and hack the project! Make changes, introduce new features and functionalities, be part of the project!

### Using the good old e-mail:
- Not interested in Git? No problem, send an email with your files attached, in the accepted formats.
- Even simpler, are you contributing with simple text? Just write your full text in the body of the email and send it! Follow the instructions for the authors and contribute!

### Commenting on other contributions:
- Through GitHub: open an _[issue][issue]_, or
- On the project page, leave your comments.

## References:

1. Open science, open questions / Sarita Albagli, Maria Lucia Maciel & Alexandre Hannud Abdo organizers. – Brasília: IBICT; Rio de Janeiro: UNIRIO, 2015. 312 p.
2. Ioannidis, John P. A.; Fanelli, Daniele; Dunne, Debbie Drake; Goodman, Steven N. (2015). Meta-research: Evaluation and Improvement of Research Methods and Practices. PLOS Biology. 13 (10): e1002264.
3. Grey literature in library and information studies / edited by Dominic J. Farace and Joachim Schöpfel, 2010, Walter de Gruyter GmbH & Co. KG, Berlin/New York, ISBN 978-3-598-11793-0.

[atlassian]: https://www.atlassian.com/git/tutorials
[gittut]: https://try.github.io/levels/1/challenges/1
[dc]: https://www.fda.gov/RegulatoryInformation/Guidances/ucm126420.htm
[duly]: http://www.apa.org/science/leadership/care/guidelines.aspx
[white]: https://en.wikipedia.org/wiki/White_paper
[grey]: https://en.wikipedia.org/wiki/Grey_literature
[cc]: https://creativecommons.org/licenses/?lang=pt_BR
[ccby]: https://creativecommons.org/licenses/by/4.0/
[ca]: https://www.fosteropenscience.eu/content/what-open-science-introduction
[self]: https://en.wikipedia.org/wiki/Self-archiving
[post]: http://www.sherpa.ac.uk/romeoinfo.html
[preprint]: https://en.wikipedia.org/wiki/Preprint
[pull]: https://help.github.com/articles/creating-a-pull-request-from-a-fork/
[issue]: https://guides.github.com/features/issues/
[githubp]: https://pages.github.com
[github]: https://github.com
[git]: https://git-scm.com
[doi]: https://doi.org
[meta]: https://en.wikipedia.org/wiki/Meta-research
[zenodo]: https://zenodo.org
[figshare]: https://figshare.com
[pandoc]: https://pandoc.org
[sherpa]: http://www.sherpa.ac.uk/romeo/index.php?la=pt&fIDnum=|&mode=simple
[mail]: mailto:valkyr.ie@outlook.com
[twit]: https://twitter.com/fhcflx
[markdown]: https://daringfireball.net/projects/markdown/syntax
[slide]: https://www.slideshare.net
[youtube]: https://www.youtube.com
[gpg]: https://www.gnupg.org/gph/en/manual/c14.html

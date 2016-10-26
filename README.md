# Text unshredding using an ATSP solver

## Introduction

Recently I came across
 [robinhouston's image unshredding algorithm](https://github.com/robinhouston/image-unshredding) and it
blew my mind. His idea was to solve the problem of *unshredding* an image by
modelling it as an instance of the [Travelling Salesman
Problem](https://en.wikipedia.org/wiki/Travelling_salesman_problem). This happened to
work beautifully on images, which kept me thinking if the same would hold true for text...

## Text unshredding is an instance of the Asymmetric Travelling Salesman Problem

Given a *shredded* text (one were its columns have been shuffled), the task of
reconstructing or *unshredding* consists in finding the correct order for
each of these columns.

Similar to what Robin did, we could think of the columns as nodes in a weighted
directed graph, were each edge corresponds to a measure of dissimilarity between
them. By searching for a Hamiltonian path of minimum weight in the directed
graph we are left with an instance of the Asymmetric Travelling Salesman Problem
which returns an ordering of the columns with least dissimilarity.

### Why Asymmetric?

Unlike image unshredding, when measuring dissimilarity between columns of text,
order does matter. A column doesn't necessarily hold the same dissimilarity
score when placed before rather than after another one. This has to do with the
dissimilarity measure chosen. Therefore, a weighted directed graph is needed with edges
coming and going between each pair of nodes with independent weights.

## Dissimilarity measure

This project uses the information provided by the conditional probability of
one letter following another. By calculating it for each row in a pair of
columns one can measure how probable it is that they're together.

To my convenience, a blogger named [David Taylor
had already published an
article](http://www.prooffreader.com/2014/09/how-often-does-given-letter-follow.html)
where he shared these frequencies.

## Results

What at first glance seems to be a jumble of letters...

```
wer bcntrtorr sideoa a dg.toe lineis  hkc tt hgseid t,I i AisihnkycrwnWala ptn l
f rahnr,is e ed ei lfbSupe aoz eivhe itsn  o t ttizd snhcntsthcn en mlwin,ioha i
 fasutoyi h aolhrt hyoiohqlcMuiseohrs o,tuuodgkencgtn sd  gcislko Vnp ipr  lytqs
rfns edlpt irta u lie o iTn ismno.ht n gthhly ehg wlmte  f raivhnroou egatrgewot
na g Areo eldatgarrbo y  da ec.feuo nim l   dc meoaaolwei afd bstbso epsdltnotto
 thegdbyenni, lsee  o tot  etoklptpt   .isdadef emrica,l la w op dclodiodaayrIrh
  fdufwese tmavaio, e  o tn orennfucae: ,ybmeofo feh raro a  eaiathaer-nmmt cfot
eyfeedg adcoairagmtumui Wdwn maec toallsaenursy efotn  a.hevtn osshrta hk   b hd
t ef. ld t  gilti os   otaenh e rtstba.ossmseeta su ihhifyiIe  eaevtsw tnrEnw st
 ru , ir c aenu cisesrwrih tcen tlda audttgft nkthstycmiuheaoldownefog rpnr  rge
fprppinsarter. o lec iIekt to a mfhnHfeW   t Ttw aen e.aey rai sooretaw hsadoe v
nt htn esin hcvotc nasn ireidWn nle a rva o asulhbituwvia,  dopoes-a eafdgyw,rh 
seos tggaewer nw h,sensn.li  tl lc m ,vw aOhinkind oathgay,nteliilae  nrehr eyts
m ui e ltttrpel w .frrpszho oheetmfo ih fedae esswa,ot ighehfo anthcpt o-tt laes
eo entaae ofwy urlbiv teewInd otrl ihtshh ethsoatoptoc sees ahfurcc  oyws     oi
eGcHy,TnoI.  eIOC s hAtBnauU IOnTthtpvN enaiWt ha GRi oebHEutIm  BYo r.w n Roe S
 ufglliia u shhcndnvtdetwsd oyareahsffoeroigac h e iheies wti atio u  mti ta  fr
 Taniorlt.po  poo aceitone vcd onglcee m tof-b dmluinggo  oh pt iteroma r hfhawi
strpatdl a g eaw -lo eeihau urfohtieaerfdn emruif r hrqk icdcflwhro  hdlme hlt o
hate oitt aoths csitwoWstw saw uadwe dsg eehv rs,eihr .thnduthn mckoi rn on e ne
,eiegrtmu ecmeinhlmen(  l lc Ts su e btclbda )sst hiotltatriwehde esddei.ilualnn
tflthm ie  eudwoitnaeg,oe doe c f vl.aomst Hnoeuyew rieto sr t  py e ohbn fhwvtt
in gaoe lrfp yygast hmwalzo sismuam o,ee e y eiab lihed rreldtsbffs :id rse,hemh
tf.mv ohe wvew rryi rf i feeychher aHsoa aasisau rheenhei tri l,pwt b ilh  hlrou
oerutbrlugsu db,o aic fnna  agda tl eyhp z snbaesruenis  hir sl yneoarocannslaak
.u~dhnh~e o~ ~~ia~~ed s ~~ee t ~n~~e~dj~ ~~~t~cn~~hw~add~te ~to~d t~ ~~af srl~th
```

...happens to be Orwell's *1984* first paragraphs!
```
It was a bright cold day in April, and the clocks were striking thirteen. Winsto
n Smith, his chin nuzzled into his breast in an effort to escape the vile wind, 
slipped quickly through the glass doors of Victory Mansions, though not quickly 
enough to prevent a swirl of gritty dust from entering along with him.  The hall
way smelt of boiled cabbage and old rag mats. At one end of it a coloured poster
, too large for indoor display, had been tacked to the wall. It depicted simply 
an enormous face, more than a metre wide: the face of a man of about forty-five,
 with a heavy black moustache and ruggedly handsome features. Winston made for t
he stairs. It was no use trying the lift. Even at the best of times it was seldo
m working, and at present the electric current was cut off during daylight hours
. It was part of the economy drive in preparation for Hate Week. The flat was se
ven flights up, and Winston, who was thirty-nine and had a varicose ulcer above 
his right ankle, went slowly, resting several times on the way. On each landing,
 opposite the lift-shaft, the poster with the enormous face gazed from the wall.
 It was one of those pictures which are so contrived that the eyes follow you ab
out when you move. BIG BROTHER IS WATCHING YOU, the caption beneath it ran.  Ins
ide the flat a fruity voice was reading out a list of figures which had somethin
g to do with the production of pig-iron. The voice came from an oblong metal pla
que like a dulled mirror which formed part of the surface of the right-hand wall
. Winston turned a switch and the voice sank somewhat, though the words were sti
ll distinguishable. The instrument (the telescreen, it was called) could be dimm
ed, but there was no way of shutting it off completely. He moved over to the win
dow: a smallish, frail figure, the meagreness of his body merely emphasized by t
he blue overalls which were the uniform of the party. His hair was very fair, hi
s face naturally sanguine, his skin roughened by coarse soap and blunt razor bla
des and the cold of the winter that had just ended. ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
```

This is an example of a completely successful reconstruction, which depends in
several factors that need to be taken into account.

### Rows and columns

The number of rows in a shredded text depends on the chosen width (number of
columns). With more rows, each column has more data which results in computing a
more accurate score. To serve as an example, here is what happens
if we only shred the first paragraph of the previous text.

**Shredded**

```
na lassind  tnr  lao,gine yo.  akithirclIh tseci kgcnio er dAepe  twbhrtrttWwdsi
ll  ,tdhnuaisrr inb s hithe e fi  hcienintz,eoneSspnasaei netvo d ofht  i  wmztc
 hqi ilskos  oau roh khend  qsypohylc tssouyrMtsi,hVtccota rgolftdo ugnniulipge 
~iomta~i~ sntdn~ra  tehog r~~ egn ev~iete s~titnogiowr t rfu .gflylr  omphn~uwh
```

**Reconstructed**
```
wallIwg corike rthe thin as blcsty trond d ing catherpe rd. Winostn is Aiike,t a
min nf in is the t S thinbe hinthe s aruze capinlocorove ze win d,ld tathesis f,
ppris k thicond lofinghe orqusVey s acoourd th tholMaloongquick ly thisgss,t uy 
ugamerere prng in fom hof to toher tr d suy wintilving.tow~~~~~~~~~l as ing thet
```

**Original**
```
It was a bright cold day in April, and the clocks were striking thirteen. Winsto
n Smith, his chin nuzzled into his breast in an effort to escape the vile wind, 
slipped quickly through the glass doors of Victory Mansions, though not quickly 
enough to prevent a swirl of gritty dust from entering along with him. ~~~~~~~~~
```

Even though the result is far from what it's supposed to look, it's interesting
to see how some words like `thin`, `in` or `the` have been naturally formed.

### Text symbols

The matrix with conditional probabilities used only considers lower case letters
and spaces. As my intention was to modify as little as possible the input,
instead of removing all symbols these were mapped to the frequencies given by
the space character. This has the benefit of not losing all special
characters but inevitably generates noise by assuming they have the exact
conditional probabilities of a space character.

Therefore, the chosen text and how many special characters it has needs to be
taken into consideration when studying the end result.

## Running the code

* Clone the repository
* Run `make` to shred the texts, and download and compile
  [LKH](http://webhotel4.ruc.dk/~keld/research/LKH/).
* Now you can run `make reconstruct` to reconstruct the texts from their
  shredded versions using LKH.

## Prerequisites

You will need a working build environment (Make and a C compiler), and `curl` is
used to download files from the web.

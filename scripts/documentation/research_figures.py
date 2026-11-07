"""Research figures from the preserved notebook, recorded tables and source media.

No training, inference or annotation changes. The model drawing is schematic.
"""
import base64
import csv
from io import BytesIO
import json
from pathlib import Path
import re
from xml.etree import ElementTree as ET

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Polygon, FancyArrowPatch
from matplotlib.path import Path as MplPath
from PIL import Image
import numpy as np

ROOT=Path(__file__).resolve().parents[2]
A=ROOT/'assets'
INK='#222b34'; MUTED='#526170'; RULE='#cbd3db'
BLUE='#356a94'; TEAL='#2a7566'; PALE='#d7e5f1'; SIDE='#adc8de'
GREEN='#dbece5'; GSIDE='#a9c9bd'
plt.rcParams.update({'font.family':'STIXGeneral','mathtext.fontset':'stix',
    'font.size':13,'text.color':INK,'axes.labelcolor':INK,'xtick.color':MUTED,
    'ytick.color':INK,'axes.edgecolor':RULE,'svg.fonttype':'path',
    'svg.hashsalt':'urinary-crystal-research','savefig.facecolor':'white'})

def t(ax,x,y,s,size=13,**kw):
    return ax.text(x,y,s,fontsize=size,ha=kw.pop('ha','center'),
                   va=kw.pop('va','center'),**kw)

def arrow(ax,points,color=INK,lw=1):
    ax.add_patch(FancyArrowPatch(path=MplPath(points),arrowstyle='-|>',
                                mutation_scale=11,color=color,lw=lw))

def volume(ax,x,y,w,h,d,fill=PALE,side=SIDE):
    dx,dy=d,-d*.5
    for points,c in [([(x,y-h/2),(x+w,y-h/2),(x+w+dx,y-h/2+dy),(x+dx,y-h/2+dy)],fill),
                     ([(x+w,y-h/2),(x+w+dx,y-h/2+dy),(x+w+dx,y+h/2+dy),(x+w,y+h/2)],side)]:
        ax.add_patch(Polygon(points,facecolor=c,edgecolor=INK,lw=.65))
    ax.add_patch(Rectangle((x,y-h/2),w,h,facecolor=fill,edgecolor=INK,lw=.7))

def box(ax,x,y,w,h,lines,fill='#f6f8fa',size=13):
    ax.add_patch(Rectangle((x,y),w,h,facecolor=fill,edgecolor=INK,lw=.7))
    t(ax,x+w/2,y+h/2,lines,size,linespacing=1.35)

def save(fig,name):
    fig.savefig(A/(name+'.svg'),metadata={'Date':None})
    plt.close(fig)

def model_evidence():
    cells=json.loads((ROOT/'notebooks/PRI_train.ipynb').read_text())['cells']
    s=''.join(''.join(o.get('text',[])) for o in cells[37].get('outputs',[]))
    s=re.sub(r'\x1b\[[0-9;]*[mK]','',s)
    rows=[]
    for line in s[s.index('                   from'):s.index('Transferred')].splitlines():
        m=re.match(r'^\s*(\d+)\s+(.*?)\s+(\d+)\s+(\d+)\s+(\S+)\s+(\[.*\])\s*$',line)
        if m:rows.append(dict(layer=int(m[1]),from_layers=m[2].strip(),repeats=int(m[3]),
                             parameters=int(m[4]),module=m[5],arguments=m[6]))
    assert len(rows)==24
    assert sum(r['parameters'] for r in rows)==22370781
    assert rows[-1]['arguments']=='[15, 32, 256, 16, None, [256, 512, 512]]'
    assert '22,370,781 parameters' in s
    with (ROOT/'results/yolo11m-layer-summary.csv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]),lineterminator='\n');w.writeheader();w.writerows(rows)

def method():
    fig,ax=plt.subplots(figsize=(12,7.15));fig.subplots_adjust(left=0,right=1,bottom=0,top=1)
    ax.set(xlim=(0,1200),ylim=(715,0));ax.axis('off')
    t(ax,25,28,'(a) Dataset preparation and validation design',18,ha='left',weight='bold')
    raw=Image.open(A/'source/microscopy-example.jpg')
    ax.imshow(raw,extent=(30,164,155,71),interpolation='nearest')
    t(ax,98,178,'Microscopy images',12)
    t(ax,98,200,'+ expert polygons',12)
    arrow(ax,[(175,116),(224,116)])
    t(ax,382,82,'Annotation preparation',15,weight='bold')
    t(ax,382,116,'Match images and polygons',13)
    t(ax,382,145,'Merge aliases · filter sparse classes',13)
    t(ax,382,174,'RGBA → RGB working copies',13)
    t(ax,382,201,'41 IDs → 36 canonical → 19 supported → 15 retained',11.5,color=MUTED)
    arrow(ax,[(533,116),(589,116)])
    volume(ax,609,116,29,67,22)
    t(ax,673,88,'Prepared dataset',15,ha='left',weight='bold')
    t(ax,673,121,'583 images · 15 classes',13,ha='left')
    t(ax,673,151,'7,371 annotated instances',13,ha='left')
    arrow(ax,[(859,116),(907,116)])
    t(ax,1035,71,'Five validation folds',15,weight='bold')
    for r in range(5):
        for c in range(5):
            ax.add_patch(Rectangle((941+c*35,92+r*18),31,14,
                facecolor=GREEN if c==r else '#e7edf3',edgecolor='white',lw=.5))
    t(ax,1027,200,'Multilabel stratification · seed 42',12)
    ax.add_patch(Rectangle((923,218),10,10,facecolor=GREEN,edgecolor=RULE,lw=.5))
    t(ax,942,223,'Validation',11,ha='left')
    ax.add_patch(Rectangle((1044,218),10,10,facecolor='#e7edf3',edgecolor=RULE,lw=.5))
    t(ax,1063,223,'Training',11,ha='left')
    t(ax,25,251,'Filename metadata supports the data audit; it is not an additional model input.',12,ha='left',color=MUTED)
    ax.plot([25,1175],[274,274],color=RULE,lw=.8)

    t(ax,25,302,'(b) YOLO11m-seg: multiscale features and instance masks',18,ha='left',weight='bold')
    t(ax,25,332,r'Input: $1024\times1024\times3$  ·  Fine-tuned pretrained weights  ·  22,370,781 parameters in the recorded 15-class model',12,ha='left',color=MUTED)

    # Backbone feature hierarchy, followed by the verified neck outputs.
    t(ax,112,368,'Backbone',15,weight='bold')
    t(ax,112,392,'Conv · C3k2',12)
    t(ax,112,414,'SPPF · C2PSA',12)
    for y,h,name in [(466,58,r'$P_3/8$'),(547,43,r'$P_4/16$'),(626,29,r'$P_5/32$')]:
        volume(ax,60,y,38,h,25)
        t(ax,136,y,name,13)
    arrow(ax,[(77,497),(77,517)]);arrow(ax,[(77,571),(77,605)])
    # Separate lanes make all three feature paths visible.
    box(ax,232,431,208,225,'Feature fusion\n\nUpsample + concatenate\nC3k2\nDownsample + concatenate',size=13)
    for y in [466,547,626]:arrow(ax,[(172,y),(228,y)])
    t(ax,548,391,'Neck outputs',15,weight='bold')
    for y,h,label in [(466,44,r'$128\times128\times256$'),(547,32,r'$64\times64\times512$'),(626,23,r'$32\times32\times512$')]:
        arrow(ax,[(444,y),(479,y)])
        volume(ax,488,y,29,h,21,GREEN,GSIDE)
        t(ax,547,y+37,label,12)
    # All scales feed box/class and coefficient prediction. P3 also feeds Proto.
    for y in [466,547,626]:
        ax.plot([547,639,639],[y,y,482],color=MUTED,lw=.8)
    arrow(ax,[(639,482),(679,482)])
    box(ax,685,436,221,88,'Box + class prediction\n15 class scores / candidate\n32 mask coefficients',size=13)
    arrow(ax,[(547,466),(620,466),(620,590),(679,590)],color=TEAL)
    box(ax,685,557,221,66,'Prototype branch (P3)\n32 maps at 256 × 256',fill='#edf5f0',size=13)
    arrow(ax,[(910,480),(966,480)])
    arrow(ax,[(910,590),(948,590),(948,541),(966,541)],color=TEAL)
    box(ax,972,448,200,112,'Decode + NMS\nCombine coefficients\nwith prototypes\nCrop / resize masks',size=13)
    arrow(ax,[(1072,565),(1072,601)])
    t(ax,1072,622,r'Instances: $(M_i,\ c_i,\ s_i)$',15,weight='bold')
    t(ax,1072,648,'Mask · class · confidence',12)
    t(ax,25,695,'Tensor labels: H × W × C. The architecture is provided by Ultralytics; volumes and fold cells are schematic.',11.5,ha='left',color=MUTED)
    save(fig,'workflow')

# The two README diagrams use live SVG text so labels match the surrounding page.
FIG_INK = '#1d324b'
FIG_MUTED = '#4b627b'
FIG_RULE = '#8499af'
FIG_BLUE = '#295e9e'
FIG_TRAIN = '#e5edf7'
FIG_VAL = '#cae6dc'
FIG_VAL_INK = '#196551'
FIG_UNANNOTATED = '#d6d9de'


def diagram(height, title, description):
    svg = ET.Element('svg', {
        'xmlns': 'http://www.w3.org/2000/svg', 'width': '800', 'height': str(height),
        'viewBox': f'0 0 800 {height}', 'role': 'img', 'aria-labelledby': 'title desc',
        'font-family': 'Arial, Helvetica, sans-serif', 'fill': FIG_INK,
    })
    ET.SubElement(svg, 'title', id='title').text = title
    ET.SubElement(svg, 'desc', id='desc').text = description
    rect(svg, 0, 0, 800, height, 'white')
    return svg


def rect(svg, x, y, w, h, fill, radius=0, stroke='none'):
    ET.SubElement(svg, 'rect', x=str(x), y=str(y), width=str(w), height=str(h),
                  rx=str(radius), fill=fill, stroke=stroke)


def label(svg, x, y, value, size=15, *, color=FIG_INK, bold=False, anchor='start'):
    ET.SubElement(svg, 'text', {
        'x': str(x), 'y': str(y), 'font-size': str(size), 'font-weight': '600' if bold else '400',
        'fill': color, 'text-anchor': anchor,
    }).text = str(value)


def connector(svg, path, *, arrowhead=False):
    attrs = {'d': path, 'stroke': FIG_RULE, 'fill': 'none', 'stroke-width': '1.5',
             'stroke-linecap': 'round', 'stroke-linejoin': 'round'}
    if arrowhead:
        attrs['marker-end'] = 'url(#arrow)'
    ET.SubElement(svg, 'path', attrs)


def write_diagram(svg, name):
    ET.indent(svg)
    (A / name).write_text(ET.tostring(svg, encoding='unicode') + '\n', encoding='utf-8')


def microscopy_tile(svg, image, x, y, width, height):
    buffer = BytesIO()
    image.save(buffer, format='JPEG', quality=92)
    encoded = base64.b64encode(buffer.getvalue()).decode('ascii')
    ET.SubElement(svg, 'image', x=str(x), y=str(y), width=str(width), height=str(height),
                  href=f'data:image/jpeg;base64,{encoded}')


def mask_head():
    svg = diagram(236, 'How YOLO11m-seg outlines a single crystal',
                  'The marked crystal in the input field corresponds to the enlarged prediction on the right. '
                  'YOLO11m-seg combines 32 prototype maps shared across the image using 32 weights for one detection.')
    marker = ET.SubElement(ET.SubElement(svg, 'defs'), 'marker', {
        'id': 'arrow', 'viewBox': '0 0 8 8', 'refX': '7', 'refY': '4',
        'markerWidth': '6', 'markerHeight': '6', 'orient': 'auto',
    })
    ET.SubElement(marker, 'path', d='M1 1L7 4L1 7', fill='none', stroke=FIG_RULE)

    label(svg, 16, 32, 'Microscopy field', 18, bold=True)
    source = ROOT / 'data/annotated/images/train/cristaux_01/Database/weddellite octaedrique/C2_taill_heter_lb.jpg'
    with Image.open(source) as field:
        field.thumbnail((390, 265))
        microscopy_tile(svg, field, 16, 64, 192, 130)
    # Visual locator on the source field, not a model-generated detection box.
    ET.SubElement(svg, 'circle', cx='129', cy='178', r='13', fill='none',
                  stroke='white', attrib={'stroke-width': '4'})
    ET.SubElement(svg, 'circle', cx='129', cy='178', r='13', fill='none',
                  stroke=FIG_BLUE, attrib={'stroke-width': '2'})
    label(svg, 16, 219, 'Circled crystal: weddellite', 14, color=FIG_MUTED)

    connector(svg, 'M211 111H225Q230 111 230 106V79Q230 74 235 74H248', arrowhead=True)
    connector(svg, 'M211 135H225Q230 135 230 140V170Q230 175 235 175H248', arrowhead=True)
    rect(svg, 256, 39, 255, 73, '#f0f5fb', radius=9)
    label(svg, 270, 67, 'Once per image', 17, bold=True)
    label(svg, 270, 93, '32 prototype maps at 256 × 256', 15, color=FIG_MUTED)
    rect(svg, 256, 139, 255, 73, '#f0f5fb', radius=9)
    label(svg, 270, 167, 'For the circled crystal', 17, bold=True)
    label(svg, 270, 193, 'A box and 32 mask weights', 15, color=FIG_MUTED)

    connector(svg, 'M515 75H531Q536 75 536 80V115Q536 120 541 120H559', arrowhead=True)
    connector(svg, 'M515 175H531Q536 175 536 170V136Q536 131 541 131H559', arrowhead=True)
    rect(svg, 567, 39, 217, 173, '#eef7f3', radius=9)
    label(svg, 581, 65, 'One instance mask', 17, color=FIG_VAL_INK, bold=True)
    with Image.open(A/'validation-predictions.jpg') as report:
        # The lower crystal in report Figure 6.3, row 2, column 3.
        zoom = report.crop((1606, 816, 1701, 880))
        microscopy_tile(svg, zoom, 581, 81, 108, 73)
    label(svg, 581, 177, 'Combine the maps, then', 15, color=FIG_MUTED)
    label(svg, 581, 197, 'crop to the predicted box.', 15, color=FIG_MUTED)
    write_diagram(svg, 'single-crystal-mask.svg')


def split_figure():
    directory = ROOT / 'data' / 'annotated'
    splits = []
    for name in ('train', 'val', 'test'):
        lines = (directory / f'{name}_split.txt').read_text().splitlines()
        splits.append(sum(bool(line.strip()) for line in lines))

    cells = json.loads((ROOT / 'notebooks/PRI_train.ipynb').read_text())['cells']
    output = ''.join(''.join(item.get('text', [])) for item in cells[36]['outputs'])
    sizes = [(int(fold), int(train), int(val)) for fold, train, val in
             re.findall(r'Fold (\d+): train=(\d+) val=(\d+)', output)]
    with (ROOT / 'results/recorded-fold-metrics.csv').open() as stream:
        results = {row['fold']: (int(row['epoch']), float(row['mask_map50_95']))
                   for row in csv.DictReader(stream) if row['experiment'] == 'yolo11m_drop4_15_classes'}
    total = sum(val for _, _, val in sizes)
    assert [fold for fold, _, _ in sizes] == list(range(1, 6))
    assert all(train + val == total for _, train, val in sizes)

    svg = diagram(384, 'Image splits and five-fold cross-validation',
                  'The first panel divides the original collection by use. In the second panel, '
                  'each highlighted group is held out once. Scores are from each fold’s best epoch.')
    label(svg, 16, 28, '(a) Initial image split', 19, bold=True)
    label(svg, 784, 28, f'{sum(splits)} source images', anchor='end', color=FIG_MUTED)
    x = 16
    colors = (FIG_TRAIN, FIG_VAL, FIG_UNANNOTATED)
    for count, color in zip(splits, colors):
        width = 768 * count / sum(splits)
        rect(svg, x, 47, width-1, 17, color)
        x += width
    for x, count, name, color in zip((16, 283, 557), splits,
                                     ('training', 'validation', 'unannotated'), colors):
        rect(svg, x, 82, 12, 12, color, radius=3)
        label(svg, x+20, 93, f'{count} {name}', color=FIG_MUTED)
    rect(svg, 16, 115, 768, 1, '#d6e0ea')

    label(svg, 16, 146, '(b) Five-fold cross-validation', 19, bold=True)
    label(svg, 784, 146, f'{total} prepared images', anchor='end', color=FIG_MUTED)
    label(svg, 16, 171, 'YOLO11m-seg   ·   15 classes   ·   multilabel stratification by image',
          14, color=FIG_MUTED)
    left, grid_width = 91, 276
    label(svg, left, 204, 'Held-out images', 14, bold=True)
    for x, title in [(444, 'Training images'), (570, 'Best epoch'), (711, 'Mask mAP50–95')]:
        label(svg, x, 204, title, 14, bold=True, anchor='middle')
    for row, (fold, train, _) in enumerate(sizes):
        y = 222 + 32 * row
        label(svg, 16, y+16, f'Fold {fold}', bold=True)
        x = left
        for group, _, val in sizes:
            width = grid_width * val / total
            held_out = group == fold
            rect(svg, x, y, width-3, 22, FIG_VAL if held_out else FIG_TRAIN, radius=4,
                 stroke='#78ab98' if held_out else 'none')
            if held_out:
                label(svg, x+(width-3)/2, y+16, val, 14, bold=True, color=FIG_VAL_INK, anchor='middle')
            x += width
        epoch, score = results[f'fold_{fold}']
        for x, value in [(444, train), (570, epoch), (711, f'{score:.5f}')]:
            label(svg, x, y+16, value, anchor='middle')
    write_diagram(svg, 'validation-fold-layout.svg')


def support_chart():
    with (ROOT/'metadata/derived/drop4-class-support.csv').open() as f:rows=list(csv.DictReader(f))
    rows.sort(key=lambda r:int(r['images']),reverse=True)
    fig,axes=plt.subplots(1,2,figsize=(10,5.1));fig.subplots_adjust(left=.14,right=.96,bottom=.13,top=.89,wspace=.25)
    for ax,col,title,color in zip(axes,['images','instances'],['(a) Images containing the class','(b) Annotated instances'],[BLUE,TEAL]):
        values=[int(r[col]) for r in rows];ax.barh(range(15),values,color=color,height=.62);ax.invert_yaxis()
        ax.set_yticks(range(15),[r['class_name'].split('_')[0] for r in rows] if col=='images' else ['']*15)
        ax.set_title(title,fontsize=13,pad=12);ax.spines[['left','top','right']].set_visible(False);ax.tick_params(axis='y',length=0)
        ax.set_xlim(0,max(values)*1.18)
        for i,v in enumerate(values):ax.text(v+max(values)*.02,i,str(v),va='center',fontsize=10.5)
    save(fig,'class-support')

def annotation_example():
    stem='cristaux_01/Database/weddellite octaedrique/C2_taill_heter_lb'
    im=Image.open(ROOT/f'data/annotated/images/train/{stem}.jpg').convert('RGB')
    lines=(ROOT/f'data/annotated/labels/train/{stem}.txt').read_text().splitlines()
    assert re.search(r'15:\s*C2_weddellite',(ROOT/'data/annotated/data.yaml').read_text())
    polygons=[]
    for line in lines:
        values=line.split();assert int(values[0])==15
        xy=np.array(list(map(float,values[1:]))).reshape(-1,2)
        assert np.all((xy>=0)&(xy<=1))
        xy*=np.array(im.size);polygons.append(xy)
    assert len(polygons)==7
    fig,axes=plt.subplots(1,2,figsize=(10,3.45))
    fig.subplots_adjust(left=.01,right=.99,bottom=.035,top=.86,wspace=.035)
    for ax,title in zip(axes,['(a) Original microscopy field','(b) Expert polygons · C2 (weddellite)']):
        ax.imshow(im);ax.set(xticks=[],yticks=[]);ax.set_title(title,fontsize=13,pad=11)
        for sp in ax.spines.values():sp.set_color(RULE);sp.set_linewidth(.6)
    for xy in polygons:
        axes[1].add_patch(Polygon(xy,closed=True,facecolor=TEAL,alpha=.22,edgecolor='none'))
        axes[1].add_patch(Polygon(xy,closed=True,fill=False,edgecolor='#e9fff5',lw=1.1))
    save(fig,'annotation-example')

    with Image.open(A/'validation-predictions.jpg') as report:
        # Figure 6.3 is a 3-column collage. Row 2, column 3 is the same C2 field.
        assert report.size == (1920, 1341)
        prediction = report.crop((1280, 448, 1920, 896))
    preview_panel(im, 'Expert annotation', 'Seven C2 polygons', 'weddellite-expert', polygons)
    preview_panel(prediction, 'Model prediction', 'Report figure 6.3', 'weddellite-prediction')


def preview_panel(image, title, subtitle, filename, polygons=()):
    fig = plt.figure(figsize=(4.8, 3.9))
    fig.text(.025, .925, title, fontsize=16, weight='bold', fontfamily='DejaVu Sans')
    fig.text(.025, .855, subtitle, fontsize=12, color=MUTED, fontfamily='DejaVu Sans')
    ax = fig.add_axes([.025, .025, .95, .78])
    ax.imshow(image)
    for xy in polygons:
        ax.add_patch(Polygon(xy, closed=True, facecolor='#23b897', alpha=.25, lw=0))
        ax.add_patch(Polygon(xy, closed=True, fill=False, edgecolor='#effff9', lw=1.2))
    ax.axis('off')
    fig.savefig(A/f'{filename}.jpg', dpi=175, pil_kwargs={'quality': 93})
    plt.close(fig)

if __name__=='__main__':
    model_evidence();method();mask_head();split_figure();support_chart();annotation_example()
    print('Extracted model summary; generated five figures and two microscopy previews.')

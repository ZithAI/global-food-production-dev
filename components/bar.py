from pyecharts.charts import Bar
from pyecharts import options as opts


from htmltools import HTML


def bar_base() -> Bar:
    bar = (
        Bar()
        .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
        .add_yaxis("A", [5, 20, 36, 10, 75, 90])
        .add_yaxis("B", [15, 25, 16, 55, 48, 8])
        .set_global_opts(title_opts=opts.TitleOpts(title="Bar-基本示例", subtitle="我是副标题"))
    )
    return bar.render_embed()

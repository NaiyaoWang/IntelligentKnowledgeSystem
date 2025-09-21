import gradio as gr

# 默认URL配置
default_urls = {
    "文库问答": "http://192.168.0.25:8080/chat/a08bc3b1415976e2",
    "文档校正": "http://192.168.0.25:8080/chat/c824e78d6d506896",
    "问数": "http://192.168.0.25:8000/xpack_static/sqlbot-embedded-dynamic.umd.js",
    "自由问答": "http://192.168.0.25:8080/chat/e57e2ce545242335"
}

# 问数页面的特殊处理函数（已更新）
def get_wenshu_html(embedded_id="7375473178857967616"):
    return f"""
    <div class="copilot"></div>
    <script>
    (function(){{
        const script = document.createElement('script');
        script.defer = true;
        script.async = true;
        script.src = "http://192.168.0.25:8000/xpack_static/sqlbot-embedded-dynamic.umd.js";
        document.head.appendChild(script);
    }})();
    let sqlbot_embedded_timer = setInterval(() => {{
        if (window.sqlbot_embedded_handler?.mounted) {{
            window.sqlbot_embedded_handler.mounted('.copilot', {{ "embeddedId": "{embedded_id}" }});
            clearInterval(sqlbot_embedded_timer);
        }}
    }}, 1000);
    </script>
    """

# 创建iframe HTML代码
def create_iframe(url):
    return f"""
    <iframe 
        src="{url}" 
        style="width: 100%; height: 800px; border: none;" 
        frameborder="0" 
        allow="microphone">
    </iframe>
    """

# 管理页面的输入组件
def management_interface():
    with gr.Column():
        gr.Markdown("## 页面URL管理")
        urls = []
        for name in ["文库问答", "文档校正", "问数", "自由问答"]:
            url = gr.Textbox(
                label=name,
                value=default_urls[name],
                interactive=True
            )
            urls.append(url)
        
        save_btn = gr.Button("保存配置")
        output = gr.Textbox(label="状态", interactive=False)
        
        return urls + [save_btn, output]

# 主应用
with gr.Blocks(title="多功能问答平台") as demo:
    with gr.Tabs():
        # 标签页1: 文库问答
        with gr.Tab("文库问答"):
            gr.HTML(create_iframe(default_urls["文库问答"]))
        
        # 标签页2: 文档校正
        with gr.Tab("文档校正"):
            gr.HTML(create_iframe(default_urls["文档校正"]))
        
        # 标签页3: 问数
        with gr.Tab("问数"):
            gr.HTML(get_wenshu_html("7375473178857967616"))  # 使用新的embeddedId
        
        # 标签页4: 自由问答
        with gr.Tab("自由问答"):
            gr.HTML(create_iframe(default_urls["自由问答"]))
        
        # 标签页5: 管理页面
        with gr.Tab("管理页面"):
            url_inputs = management_interface()

# 由于Gradio的限制，运行时URL更改需要重新启动应用
# 这里提供一个简单的管理界面示例
# 实际部署时可能需要更复杂的配置管理

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
# type: ignore
import bpy
import os

bl_info = {
    "name": "NodeGroupBake",
    "author": "xqfa",
    "description": "节点组烘焙与通道打包 — 将节点组输出烘焙为贴图并打包 DDS/TGA",
    "blender": (4, 5, 0),
    "version": (1, 0, 0),
    "location": "Node Editor > Sidebar > NodeGroupBake",
    "warning": "",
    "category": "Material",
}

from . import bake_node_groups


class NodeGroupBakePreferences(bpy.types.AddonPreferences):
    bl_idname = __package__

    def get_default_texconv_path():
        # 获取当前文件（__init__.py）所在的目录
        addon_dir = os.path.dirname(__file__)
        # 拼接目标路径：插件目录/texconv.exe
        default_path = os.path.join(addon_dir, "texconv.exe")
        return default_path

    texconv_path: bpy.props.StringProperty(
        name="texconv.exe 路径",
        subtype='FILE_PATH',
        description="用于转换 DDS 格式的工具路径",
        default=get_default_texconv_path()
    )

    def draw(self, context):
        layout = self.layout
        layout.prop(self, "texconv_path")


def register():
    bpy.utils.register_class(NodeGroupBakePreferences)
    bake_node_groups.register()


def unregister():
    bake_node_groups.unregister()
    bpy.utils.unregister_class(NodeGroupBakePreferences)


if __name__ == "__main__":
    register()

bl_info = {
    "name": "Toggle View",
    "author": "gogo",
    "version": (0, 0, 1),
    "blender": (2, 83, 1),
    "description": "Toggle viewport display",
    "warning": "",
    "support": "TESTING",
    "wiki_url": "",
    "category": "3D View"
}

import bpy
from bpy.props import (
    PointerProperty,
    BoolProperty,
    BoolVectorProperty,
    FloatVectorProperty,
    FloatProperty,
    StringProperty,
    IntProperty,
    EnumProperty
)
from bpy.types import AddonPreferences
import rna_keymap_ui


OBJECT_TYPE = [
    'MESH',
    'CURVE',
    'SURFACE',
    'FONT',
    'VOLUME',
    'GPENCIL',
    'LATTICE',
]

OBJECT_TYPE_NAME = [
    "Mesh",
    "Curve",
    "Surface",
    "Text",
    "Volume",
    "Grease Pencil",
    "Lattice",
]

MODIFIER_TYPE_MODIFY = [
    'DATA_TRANSFER',
    'MESH_CACHE',
    'MESH_SEQUENCE_CACHE',
    'NORMAL_EDIT',
    'WEIGHTED_NORMAL',
    'UV_PROJECT',
    'UV_WARP',
    'VERTEX_WEIGHT_EDIT',
    'VERTEX_WEIGHT_MIX',
    'VERTEX_WEIGHT_PROXIMITY',
]

MODIFIER_TYPE_MODIFY_NAME = [
    "Data Transfer",
    "Mesh Cache",
    "Mesh Sequence Cache",
    "Normal Edit",
    "Weighted Normal",
    "UV Project",
    "UV Warp",
    "Vertex Weight Edit",
    "Vertex Weight Mix",
    "Vertex Weight Proximity",
]

MODIFIER_TYPE_GENERATE = [
    'ARRAY',
    'BEVEL',
    'BOOLEAN',
    'BUILD',
    'DECIMATE',
    'EDGE_SPLIT',
    'MASK',
    'MIRROR',
    'MULTIRES',
    'REMESH',
    'SCREW',
    'SKIN',
    'SOLIDIFY',
    'SUBSURF',
    'TRIANGULATE',
    'WELD',
    'WIREFRAME',
]

MODIFIER_TYPE_GENERATE_NAME = [
    "Array",
    "Bevel",
    "Boolean",
    "Build",
    "Decimate",
    "Edge Split",
    "Mask",
    "Mirror",
    "Multiresolution",
    "Remesh",
    "Screw",
    "Skin",
    "Solidify",
    "Subdivision Surface",
    "Triangulate",
    "Weld",
    "Wireframe",
]

MODIFIER_TYPE_DEFORM = [
    'ARMATURE',
    'CAST',
    'CURVE',
    'DISPLACE',
    'HOOK',
    'LAPLACIANDEFORM',
    'LATTICE',
    'MESH_DEFORM',
    'SHRINKWRAP',
    'SIMPLE_DEFORM',
    'SMOOTH',
    'CORRECTIVE_SMOOTH',
    'LAPLACIANSMOOTH',
    'SURFACE_DEFORM',
    'WARP',
    'WAVE',
]

MODIFIER_TYPE_DEFORM_NAME = [
    "Armature",
    "Cast",
    "Curve",
    "Displace",
    "Hook",
    "Laplacian Deform",
    "Lattice",
    "Mesh Deform",
    "Shrinkwrap",
    "Simple Deform",
    "Smooth",
    "Smooth Corrective",
    "Smooth Laplacian",
    "Surface Deform",
    "Warp",
    "Wave",
]

MODIFIER_TYPE_SIMULATE = [
    'CLOTH',
    'COLLISION',
    'DYNAMIC_PAINT',
    'EXPLODE',
    'FLUID',
    'OCEAN',
    'PARTICLE_INSTANCE',
    'PARTICLE_SYSTEM',
    'SOFT_BODY',
]

MODIFIER_TYPE_SIMULATE_NAME = [
    "Cloth",
    "Collision",
    "Dynamic Paint",
    "Explode",
    "Fluid",
    "Ocean",
    "Particle Instance",
    "Particle System",
    "Soft Body",
]


def check_modifiers(context, mod_type):
    props = context.scene.tglview
    target_modifiers = [modifier_type for modifier_type, flag in zip(MODIFIER_TYPE_MODIFY, props.flag_modifier_type_modify) if flag is True]
    target_modifiers.extend(modifier_type for modifier_type, flag in zip(MODIFIER_TYPE_GENERATE, props.flag_modifier_type_generate) if flag is True)
    target_modifiers.extend(modifier_type for modifier_type, flag in zip(MODIFIER_TYPE_DEFORM, props.flag_modifier_type_deform) if flag is True)
    target_modifiers.extend(modifier_type for modifier_type, flag in zip(MODIFIER_TYPE_SIMULATE, props.flag_modifier_type_simulate) if flag is True)
    if mod_type in target_modifiers:
        return True
    return False


def toggle_modifiers(context, collection, bool_show):
    props = context.scene.tglview
    target_type = [object_type for object_type, flag in zip(OBJECT_TYPE, props.flag_object_type) if flag is True]
    for obj in collection.objects:
        if obj.type in target_type:
            for mod in obj.modifiers:
                if check_modifiers(context, mod.type):
                    mod.show_viewport = bool_show
    return


def toggle_shader(target, source):
    target.type = source.type
    target.background_color = source.background_color
    target.background_type = source.background_type
    target.cavity_ridge_factor = source.cavity_ridge_factor
    target.cavity_type = source.cavity_type
    target.cavity_valley_factor = source.cavity_valley_factor
    
    # target.color_type = source.color_type
    target.curvature_ridge_factor = source.curvature_ridge_factor
    target.curvature_valley_factor = source.curvature_valley_factor
    # target.cycles = source.cycles
    target.light = source.light
    target.object_outline_color = source.object_outline_color
    target.render_pass = source.render_pass
    # target.selected_studio_light = source.selected_studio_light
    target.shadow_intensity = source.shadow_intensity
    target.show_backface_culling = source.show_backface_culling
    target.show_cavity = source.show_cavity
    target.show_object_outline = source.show_object_outline
    target.show_shadows = source.show_shadows
    target.show_specular_highlight = source.show_specular_highlight
    target.show_xray = source.show_xray
    target.show_xray_wireframe = source.show_xray_wireframe
    target.single_color = source.single_color
    # target.studio_light = source.studio_light
    target.studiolight_background_alpha = source.studiolight_background_alpha
    target.studiolight_background_blur = source.studiolight_background_blur
    target.studiolight_intensity = source.studiolight_intensity
    target.studiolight_rotate_z = source.studiolight_rotate_z
    
    target.use_dof = source.use_dof
    target.use_scene_lights = source.use_scene_lights
    target.use_scene_lights_render = source.use_scene_lights_render
    target.use_scene_world = source.use_scene_world
    target.use_scene_world_render = source.use_scene_world_render
    target.use_world_space_lighting = source.use_world_space_lighting
    # target.wireframe_color_type = source.wireframe_color_type
    target.xray_alpha = source.xray_alpha
    target.xray_alpha_wireframe = source.xray_alpha_wireframe


def ui_modifier_type(self, context):
    layout = self.layout
    props = context.scene.tglview
    layout.prop(props, "toggle_modifier_type", icon="TRIA_DOWN" if props.toggle_modifier_type else "TRIA_RIGHT", text="Modifier Type", emboss=False)
    if props.toggle_modifier_type:
        column = layout.box().column(align=True)
        row = column.row(align=True)

        column = row.column(align=True)
        for index, modifier_type in enumerate(MODIFIER_TYPE_MODIFY_NAME):
            column.row().prop(props, "flag_modifier_type_modify", index=index, text=modifier_type)
        
        column = row.column(align=True)
        for index, modifier_type in enumerate(MODIFIER_TYPE_GENERATE_NAME):
            column.row().prop(props, "flag_modifier_type_generate", index=index, text=modifier_type)
        
        column = row.column(align=True)
        for index, modifier_type in enumerate(MODIFIER_TYPE_DEFORM_NAME):
            column.row().prop(props, "flag_modifier_type_deform", index=index, text=modifier_type)

        column = row.column(align=True)
        for index, modifier_type in enumerate(MODIFIER_TYPE_SIMULATE_NAME):
            column.row().prop(props, "flag_modifier_type_simulate", index=index, text=modifier_type)


def ui_object_type(self, context):
    layout = self.layout
    props = context.scene.tglview
    layout.prop(props, "toggle_object_type", icon="TRIA_DOWN" if props.toggle_object_type else "TRIA_RIGHT", text="Object Type", emboss=False)
    if props.toggle_object_type:
        box = layout.box()
        column = box.column()
        for index, object_type in enumerate(OBJECT_TYPE_NAME):
            column.row().prop(props, "flag_object_type", index=index, text=object_type)


def ui_shader_setting(self, context):
    layout = self.layout
    props = context.scene.tglview
    layout.prop(props, "toggle_shading_setting", icon="TRIA_DOWN" if props.toggle_shading_setting else "TRIA_RIGHT", text="Shading Setting", emboss=False)
    if props.toggle_shading_setting:
        layout.operator(TGLVIEW_OT_toggle_view_register.bl_idname, icon="PMARKER" if props.bSwitch_view else "PMARKER_SEL", text="Resister A").slot_index = 0
        layout.operator(TGLVIEW_OT_toggle_view_register.bl_idname, icon="PMARKER_SEL" if props.bSwitch_view else "PMARKER", text="Resister B").slot_index = 1


class TGLVIEW_OT_toggle_collection(bpy.types.Operator):
    bl_idname = "tglview.toggle_collection"
    bl_label = "Toggle Collection "
    bl_description = "Toggle Collection Visibility"
    bl_options = {'REGISTER'}

    def execute(self, context):
        collection = context.scene.tglview.oCollection_list_collection
        if collection:
            if collection.hide_viewport:
                collection.hide_viewport = False
            else:
                collection.hide_viewport = True
        
        context.view_layer.update()

        return {'FINISHED'}


class TGLVIEW_OT_toggle_view(bpy.types.Operator):
    bl_idname = "tglview.toggle_view"
    bl_label = "Toggle Shader "
    bl_description = "Toggle Shader"
    bl_options = {'REGISTER'}

    def execute(self, context):
        props = context.scene.tglview
        obj = context.object
        # モデリング時

        if props.bSwitch_view:
            props.bSwitch_view = False
            settings = context.scene.tglview_shader_0

        else:
            props.bSwitch_view = True
            settings = context.scene.tglview_shader_1

        if props.bToggle_shading:
            if props.bToggle_all_screens:
                for area in context.screen.areas:
                    if area.type == 'VIEW_3D':
                        for space in area.spaces:
                            if space.type == 'VIEW_3D':
                                toggle_shader(space.shading, settings)
            else:
                toggle_shader(context.space_data.shading, settings)

        if props.bToggle_modifier:
            if props.oCollection_list_view:
                toggle_modifiers(context, props.oCollection_list_view, props.bSwitch_view)
                if props.bRecursive_search:
                    for collection in props.oCollection_list_view.children:
                        toggle_modifiers(context, collection, props.bSwitch_view)
            else:
                for mod in obj.modifiers:
                    if check_modifiers(context, mod.type):
                        mod.show_viewport = props.bSwitch_view
        
        context.view_layer.update()

        return {'FINISHED'}


class TGLVIEW_OT_toggle_view_register(bpy.types.Operator):
    bl_idname = "tglview.toggle_view_register"
    bl_label = "Register Viewport Shading "
    bl_description = "Register Viewport Shading"
    bl_options = {'REGISTER', 'UNDO'}

    slot_index: IntProperty(default=0)

    def execute(self, context):
        if self.slot_index == 0:
            settings = context.scene.tglview_shader_0
        else:
            settings = context.scene.tglview_shader_1
        
        toggle_shader(settings, context.space_data.shading)
        return {'FINISHED'}


class TGLVIEWPanel:
    # Developer note: this is displayed in tool settings as well as the 3D view.
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Item"


class TGLVIEW_PT_collection(TGLVIEWPanel, bpy.types.Panel):
    bl_label = "Toggle Collection"
    bl_idname = "TGLVIEW_PT_collection"

    def draw(self, context):
        layout = self.layout
        props = context.scene.tglview
        layout.prop(props, property="oCollection_list_collection", text="Collection")
        layout.operator(TGLVIEW_OT_toggle_collection.bl_idname, text="Toggle Visibility")


class TGLVIEW_PT_view(TGLVIEWPanel, bpy.types.Panel):
    bl_label = "Toggle Viewport Shading"
    bl_idname = "TGLVIEW_PT_view"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout
        props = context.scene.tglview
        layout.alignment = "LEFT"
        layout.prop(props, property="oCollection_list_view", text="Collection")
        layout.operator(TGLVIEW_OT_toggle_view.bl_idname, text="Toggle Shading")
        
        layout.prop(props, property="bRecursive_search", text="Recursive Collection")
        layout.prop(props, property="bToggle_all_screens", text="Toggle All Screens")
        layout.prop(props, property="bToggle_shading", text="Toggle Viewport Shading")
        if props.bToggle_shading:
            ui_shader_setting(self, context)
        layout.prop(props, property="bToggle_modifier", text="Toggle Modifiers")
        if props.bToggle_modifier:
            ui_modifier_type(self, context)
            ui_object_type(self, context)


class TGLVIEW_props(bpy.types.PropertyGroup):
    oCollection_list_collection: PointerProperty(
        name="Collection",
        description="Collection to toggle the visibility",
        type=bpy.types.Collection,
    )
    oCollection_list_view: PointerProperty(
        name="Collection",
        description="Collection to toggle the visibility of modifiers",
        type=bpy.types.Collection,
    )
    bSwitch_view: BoolProperty(
        name="Switch view",
        description="Internal",
        default=False,
    )
    bToggle_shading: BoolProperty(
        name="bToggle_shading",
        description="Internal",
        default=True,
    )
    bToggle_modifier: BoolProperty(
        name="bToggle_modifier",
        description="Internal",
        default=True,
    )
    bToggle_all_screens: BoolProperty(
        name="bToggle_all_screens",
        description="Internal",
        default=False,
    )
    bRecursive_search: BoolProperty(
        name="Recursive Search",
        description="True: repeatedly search in collections, False: search in only 1one collection ",
        default=True,
    )
    toggle_modifier_type: BoolProperty(
        name="toggle_modifier_type",
        description="UI",
        default=False,
    )
    toggle_object_type: BoolProperty(
        name="toggle_object_type",
        description="UI",
        default=False,
    )
    toggle_shading_setting: BoolProperty(
        name="toggle_shading_setting",
        description="UI",
        default=False,
    )
    flag_object_type: BoolVectorProperty(
        name="flag_object_type",
        size=len(OBJECT_TYPE),
        default=[True,  # MESH
                 False, # CURVE
                 False, # SURFACE
                 False, # FONT
                 False, # VOLUME
                 False, # GPENCIL
                 False, # LATTICE
                ],
    )
    flag_modifier_type_modify: BoolVectorProperty(
        name="flag_modifier_type_modify",
        description="Flag for Modify modifiers",
        size=10,
    )
    flag_modifier_type_generate: BoolVectorProperty(
        name="flag_modifier_type_generate",
        description="Flag for Generate modifiers",
        size=17,
    )
    flag_modifier_type_deform: BoolVectorProperty(
        name="flag_modifier_type_deform",
        description="Flag for Deform modifiers",
        size=16,
    )
    flag_modifier_type_simulate: BoolVectorProperty(
        name="flag_modifier_type_simulate",
        description="Flag for Simulate modifiers",
        size=9,
    )


class TGLVIEW_shader(bpy.types.PropertyGroup):
    background_color :FloatVectorProperty(default=(0.05, 0.05, 0.05))
    background_type :StringProperty(default='THEME')
    cavity_ridge_factor :FloatProperty(default=1.0)
    cavity_type :StringProperty(default='SCREEN')
    cavity_valley_factor :FloatProperty(default=1.0)
    color_type :StringProperty(default='MATERIAL')
    curvature_ridge_factor :FloatProperty(default=1.0)
    curvature_valley_factor :FloatProperty(default=1.0)
    # cycles :
    light :StringProperty(default='STUDIO')
    object_outline_color :FloatVectorProperty(default=(0.0, 0.0, 0.0))
    render_pass :StringProperty(default='COMBINED')
    # selected_studio_light :
    shadow_intensity :FloatProperty(default=0.5)
    show_backface_culling :BoolProperty(default=False)
    show_cavity :BoolProperty(default=False)
    show_object_outline :BoolProperty(default=False)
    show_shadows :BoolProperty(default=False)
    show_specular_highlight :BoolProperty(default=True)
    show_xray :BoolProperty(default=False)
    show_xray_wireframe :BoolProperty(default=True)
    single_color :FloatVectorProperty(default=(0.8, 0.8, 0.8))
    studio_light :StringProperty(default='DEFAULT')
    studiolight_background_alpha :FloatProperty(default=0.0)
    studiolight_background_blur :FloatProperty(default=0.5)
    studiolight_intensity :FloatProperty(default=1.0)
    studiolight_rotate_z :FloatProperty(default=0.0)
    type :StringProperty(default='SOLID')
    use_dof :BoolProperty(default=False)
    use_scene_lights :BoolProperty(default=False)
    use_scene_lights_render :BoolProperty(default=True)
    use_scene_world :BoolProperty(default=False)
    use_scene_world_render :BoolProperty(default=True)
    use_world_space_lighting :BoolProperty(default=False)
    wireframe_color_type :StringProperty(default='MATERIAL')
    xray_alpha :FloatProperty(default=0.5)
    xray_alpha_wireframe :FloatProperty(default=0.5)


'''
Addon Preferences
'''

addon_keymaps = []
def add_hotkey():
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon

    if kc:
        km = kc.keymaps.new(name="3D View", space_type="VIEW_3D")
        kmi = km.keymap_items.new(TGLVIEW_OT_toggle_collection.bl_idname, type='U', value='PRESS', ctrl=True, alt=False, shift=True)
        addon_keymaps.append((km, kmi))

        km = kc.keymaps.new(name="3D View", space_type="VIEW_3D")
        kmi = km.keymap_items.new(TGLVIEW_OT_toggle_view.bl_idname, type='K', value='PRESS', ctrl=True, alt=True, shift=True)
        addon_keymaps.append((km, kmi))


def remove_hotkey():
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()


def update_panel(self, context):
    message = ": Updating Panel locations has failed"
    try:
        for panel in panels:
            if "bl_rna" in panel.__dict__:
                bpy.utils.unregister_class(panel)

        for panel in panels:
            panel.bl_category = context.preferences.addons[__name__.partition('.')[0]].preferences.category
            bpy.utils.register_class(panel)

    except Exception as e:
        print("\n[{}]\n{}\n\nError:\n{}".format(__name__, message, e))
        pass


class TGLVIEW_OT_reset_hotkey(bpy.types.Operator):
    ''' Add hotkey entry '''
    bl_idname = "tglview.add_hotkey"
    bl_label = "Addon Preferences Example"
    bl_options = {'REGISTER', 'INTERNAL'}

    def execute(self, context):
        wm = context.window_manager
        kc = wm.keyconfigs.addon

        if kc:
            km = kc.keymaps.get('3D View')
            if km:
                kmi = km.keymap_items.get(TGLVIEW_OT_toggle_collection.bl_idname)
                if kmi:
                    kmi.type = 'U'
                    kmi.value = 'PRESS'
                    kmi.ctrl = True
                    kmi.alt = False
                    kmi.shift = True
                else:
                    kmi = km.keymap_items.new(TGLVIEW_OT_toggle_collection.bl_idname, type='U', value='PRESS', ctrl=True, alt=False, shift=True)
                    addon_keymaps.append((km, kmi))

                kmi = kc.keymaps['3D View'].keymap_items.get(TGLVIEW_OT_toggle_view.bl_idname)
                if kmi:
                    kmi.type = 'K'
                    kmi.value = 'PRESS'
                    kmi.ctrl = True
                    kmi.alt = True
                    kmi.shift = True
                else:
                    kmi = km.keymap_items.new(TGLVIEW_OT_toggle_view.bl_idname, type='K', value='PRESS', ctrl=True, alt=True, shift=True)
                    addon_keymaps.append((km, kmi))

        self.report({'INFO'}, "Hotkey added in Preferences -> Keymap")
        return {'FINISHED'}


class TGLVIEWT_MT_AddonPreferences(AddonPreferences):
    bl_idname = __name__
    category : StringProperty(
        name="Tab Category",
        description="Tab Category name for Panels",
        default="Item", update=update_panel
    )


    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.label(text="Tab Category:")
        row.prop(self, "category", text="")

        box = layout.box()
        col = box.column()
        col.label(text="Keymap List:",icon="KEYINGSET")

        wm = bpy.context.window_manager
        kc = wm.keyconfigs.user
        for keymaps_added, keyitems_added in addon_keymaps:
            for keymaps_config in kc.keymaps:
                if keymaps_added.name == keymaps_config.name:
                    km = keymaps_config

            for kmi_con in km.keymap_items:
                if keyitems_added.name == kmi_con.name:
                    kmi = kmi_con
            try:
                col.label(text=str(km.name),icon="DOT")
                col.context_pointer_set("keymap", km)
                rna_keymap_ui.draw_kmi([], kc, km, kmi, col, 0)
                col.separator()
            except: pass
    
        col.operator(TGLVIEW_OT_reset_hotkey.bl_idname, text="Reset Keymaps")
        layout.operator("wm.url_open", text="GitHub", icon="URL").url = "https://github.com/3str6"


panels = (
    TGLVIEW_PT_collection,
    TGLVIEW_PT_view,
)


classes = (
    TGLVIEW_OT_toggle_collection,
    TGLVIEW_OT_toggle_view,
    TGLVIEW_OT_toggle_view_register,
    TGLVIEW_PT_collection,
    TGLVIEW_PT_view,
    TGLVIEW_props,
    TGLVIEW_shader,
    TGLVIEW_OT_reset_hotkey,
    TGLVIEWT_MT_AddonPreferences,
)


def register():
    for i in classes:
        bpy.utils.register_class(i)

    bpy.types.Scene.tglview = PointerProperty(type=TGLVIEW_props)
    bpy.types.Scene.tglview_shader_0 = PointerProperty(type=TGLVIEW_shader)
    bpy.types.Scene.tglview_shader_1 = PointerProperty(type=TGLVIEW_shader)
    add_hotkey()
    update_panel(None, bpy.context)


def unregister():
    del bpy.types.Scene.tglview
    del bpy.types.Scene.tglview_shader_0
    del bpy.types.Scene.tglview_shader_1
    for i in classes:
        bpy.utils.unregister_class(i)
    remove_hotkey()

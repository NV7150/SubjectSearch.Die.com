module Aspect.View exposing (..)

import Aspect.Model exposing (..)
import Html exposing (..)
import Html.Attributes exposing (..)

import Utils.Lang exposing (MultiLangText, mltext, Language)
import Model exposing (RootModel)

view : RootModel -> Html Msg
view model =
    div [ class "aspect-page" ]
        []
